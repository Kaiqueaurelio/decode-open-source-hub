(function () {
  "use strict";
  var allSoftware = [];
  var selectedCategory = "";
  var selectedStatus = "all";
  var selectedView = "grid";
  var visibleCount = 12;
  var pageSize = 12;
  var loadSequence = 0;
  var searchInput = document.getElementById("search-input");
  var filterSearchInput = document.getElementById("filter-search-input");
  var platformFilter = document.getElementById("platform-filter");
  var sortFilter = document.getElementById("sort-filter");
  var categoryChips = document.getElementById("category-chips");
  var statusTabs = document.getElementById("status-tabs");
  var softwareGrid = document.getElementById("software-grid");
  var resultCount = document.getElementById("result-count");
  var activeFilters = document.getElementById("active-filters");
  var loadMoreWrap = document.getElementById("load-more-wrap");
  var errorState = document.getElementById("error-state");
  var viewGridButton = document.getElementById("view-grid");
  var viewTableButton = document.getElementById("view-table");
  var reloadButton = document.getElementById("reload-catalog");
  var appColors = {
    photocraft:"#2f7bf5", vectorcraft:"#e8573f", filmcraft:"#8b5cf6",
    lightcraft:"#f2a516", pdfcraft:"#12a58a", effectcraft:"#e0368f",
    designcraft:"#7bb51c", figcraft:"#02da96", wordcraft:"#3f5fe0",
    soundcraft:"#1fa5c9", deckcraft:"#f07a1e", cadcraft:"#3ea6e8",
    gridcraft:"#1f9d55", "artcraft-launcher":"#d9d9d9"
  };

  function escapeHtml(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (char) {
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char];
    });
  }
  function safeUrl(value) {
    try {
      var parsed = new URL(value);
      return parsed.protocol === "https:" ? parsed.href : "";
    } catch (error) { return ""; }
  }
  function externalLink(value, label, extraClass) {
    var url = safeUrl(value);
    if (!url) return "";
    return '<a class="card-action ' + extraClass + '" href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + ' <span aria-hidden="true">↗</span></a>';
  }
  function referenceLink(value, label) {
    var url = safeUrl(value);
    if (!url) return "";
    return '<a class="card-ref-link" href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + label + ' <span aria-hidden="true">↗</span></a>';
  }
  function getCategories() {
    var counts = {};
    allSoftware.forEach(function (item) { counts[item.category] = (counts[item.category] || 0) + 1; });
    return Object.keys(counts).sort(function (a, b) { return a.localeCompare(b, "pt-BR"); }).map(function (name) {
      return {name:name,count:counts[name]};
    });
  }
  function renderCategories() {
    var categories = getCategories();
    var html = '<button class="category-chip ' + (selectedCategory === "" ? "active" : "") + '" type="button" data-category="">Todas <span class="chip-count">' + allSoftware.length + '</span></button>';
    categories.forEach(function (category) {
      html += '<button class="category-chip ' + (selectedCategory === category.name ? "active" : "") + '" type="button" data-category="' + escapeHtml(category.name) + '">' + escapeHtml(category.name) + '<span class="chip-count">' + category.count + '</span></button>';
    });
    categoryChips.innerHTML = html;
    document.getElementById("stat-total").textContent = String(allSoftware.length);
    document.getElementById("stat-categories").textContent = String(categories.length);
  }
  function statusMatches(item, status) {
    var stage = String(item.stage || "");
    if (status === "alpha") return /alpha/i.test(stage);
    if (status === "development") return /desenvolvimento/i.test(stage);
    if (status === "featured") return Boolean(item.featured);
    if (status === "utility") return item.kind === "Launcher";
    return true;
  }
  function renderStatusTabs() {
    var statuses = [
      {id:"all",label:"ALL",count:allSoftware.length},
      {id:"alpha",label:"ALPHA",count:allSoftware.filter(function(item){return statusMatches(item,"alpha");}).length},
      {id:"development",label:"EM DESENVOLVIMENTO",count:allSoftware.filter(function(item){return statusMatches(item,"development");}).length},
      {id:"featured",label:"DESTAQUES",count:allSoftware.filter(function(item){return statusMatches(item,"featured");}).length},
      {id:"utility",label:"UTILITÁRIO",count:allSoftware.filter(function(item){return statusMatches(item,"utility");}).length}
    ];
    statusTabs.innerHTML = statuses.map(function (status) {
      return '<button type="button" class="status-tab ' + (selectedStatus === status.id ? "active" : "") + '" data-status="' + status.id + '" aria-pressed="' + String(selectedStatus === status.id) + '"><span>' + status.label + '</span><b>' + status.count + '</b></button>';
    }).join("");
  }
  function renderPlatformOptions() {
    var platforms = [];
    allSoftware.forEach(function (item) {
      (item.platforms || []).forEach(function (platform) {
        if (platforms.indexOf(platform) === -1) platforms.push(platform);
      });
    });
    platforms.sort(function (a, b) { return a.localeCompare(b, "pt-BR"); });
    var old = platformFilter.value;
    platformFilter.innerHTML = '<option value="">Todas</option>' + platforms.map(function (platform) {
      return '<option value="' + escapeHtml(platform) + '">' + escapeHtml(platform) + '</option>';
    }).join("");
    platformFilter.value = platforms.indexOf(old) >= 0 ? old : "";
  }
  function currentSearch() {
    return (filterSearchInput.value || searchInput.value || "").trim().toLocaleLowerCase("pt-BR");
  }
  function getFiltered() {
    var term = currentSearch();
    var platform = platformFilter.value;
    var found = allSoftware.filter(function (item) {
      var searchable = [item.name,item.tagline,item.description,item.category,item.license,item.stage,item.kind,item.slug]
        .concat(item.tags || []).join(" ").toLocaleLowerCase("pt-BR");
      return (!term || searchable.indexOf(term) !== -1)
        && (!selectedCategory || item.category === selectedCategory)
        && (!platform || (item.platforms || []).indexOf(platform) !== -1)
        && (selectedStatus === "all" || statusMatches(item, selectedStatus));
    });
    var sort = sortFilter.value;
    found.sort(function (a, b) {
      if (sort === "name") return a.name.localeCompare(b.name, "pt-BR");
      if (sort === "category") {
        var cat = a.category.localeCompare(b.category, "pt-BR");
        return cat || a.name.localeCompare(b.name, "pt-BR");
      }
      return Number(Boolean(b.featured)) - Number(Boolean(a.featured)) || a.name.localeCompare(b.name, "pt-BR");
    });
    return found;
  }
  function renderFiltersSummary() {
    var labels = [];
    if (selectedCategory) labels.push(selectedCategory);
    if (platformFilter.value) labels.push(platformFilter.value);
    var statusLabel = {"alpha":"Alpha","development":"Em desenvolvimento","featured":"Destaques","utility":"Utilitário"}[selectedStatus];
    if (statusLabel) labels.push(statusLabel);
    if (currentSearch()) labels.push("Busca: " + currentSearch());
    activeFilters.innerHTML = labels.map(function (label) {
      return '<span class="active-filter">' + escapeHtml(label) + '</span>';
    }).join("");
  }
  function appIconMarkup(item) {
    var color = appColors[item.slug] || "#353535";
    var fallback = escapeHtml(item.icon || "◈");
    if (item.kind !== "Crafting App" || !/^[a-z0-9-]+$/.test(item.slug || "")) {
      return '<div class="app-icon" style="--app-color:' + color + '"><span class="app-icon-fallback">' + fallback + '</span></div>';
    }
    var src = "https://raw.githubusercontent.com/storytold/craft-launcher/main/assets/app-icons/" + item.slug + ".png";
    return '<div class="app-icon" style="--app-color:' + color + '"><span class="app-icon-fallback">' + fallback + '</span><img data-app-icon src="' + src + '" alt="" loading="lazy"></div>';
  }
  function wireImageFallbacks() {
    softwareGrid.querySelectorAll("img[data-app-icon]").forEach(function (img) {
      img.addEventListener("error", function () { img.hidden = true; }, {once:true});
    });
  }
  function stageMarkup(item) {
    var stage = String(item.stage || "Status não informado");
    var cls = /alpha/i.test(stage) ? "stage-alpha" : /desenvolvimento/i.test(stage) ? "stage-development" : "stage-available";
    return '<span class="stage-badge ' + cls + '">' + escapeHtml(stage) + '</span>';
  }
  function displayedName(item) {
    var name = escapeHtml(item.name || "App Decode");
    if (item.name && item.name.startsWith("Decode")) {
      return '<span class="name-accent">Decode</span>' + name.slice(6);
    }
    if (item.name && item.name.endsWith("Decode")) {
      return name.slice(0, -6) + '<span class="name-accent">Decode</span>';
    }
    return name;
  }
  function cardMarkup(item, index) {
    var color = appColors[item.slug] || "#dedede";
    var platforms = (item.platforms || []).map(function (platform) {
      return '<span class="platform-pill">' + escapeHtml(platform) + '</span>';
    }).join("");
    var licenseUrl = safeUrl(item.licenseUrl);
    var licenseMarkup = licenseUrl
      ? '<a class="license-value" href="' + escapeHtml(licenseUrl) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(item.license || "Licença") + ' ↗</a>'
      : '<span class="license-value">' + escapeHtml(item.license || "Não informada") + '</span>';
    var kindLabel = item.kind === "Launcher" ? "DECODE UTILITY" : "DECODE APP";
    var number = String(index + 1).padStart(2, "0");
    return '<article class="software-card" style="--app-color:' + color + '">'
      + '<div class="card-head"><span class="app-order">' + number + '</span><div class="card-ref-links">' + referenceLink(item.websiteUrl, "WEBSITE") + referenceLink(item.sourceUrl, "GITHUB") + '</div></div>'
      + '<div class="card-identity">' + appIconMarkup(item) + '<div class="card-name-wrap"><h3 class="card-title">' + displayedName(item) + '</h3><p class="card-tagline">' + escapeHtml(item.tagline || "") + '</p><p class="card-category">' + escapeHtml(item.category || "") + '</p></div></div>'
      + '<div class="card-status-row">' + stageMarkup(item) + '<span class="kind-pill">' + kindLabel + '</span></div>'
      + '<p class="card-description">' + escapeHtml(item.description || "") + '</p>'
      + '<div class="platform-row" aria-label="Plataformas: ' + escapeHtml((item.platforms || []).join(", ")) + '">' + platforms + '</div>'
      + '<div class="card-bottom"><div class="license-row"><span class="license-label">LICENSE</span>' + licenseMarkup + '</div><div class="card-actions">' + externalLink(item.downloadUrl, item.kind === "Launcher" ? "VER RELEASES" : "VER DOWNLOADS", "primary") + '</div></div>'
      + '</article>';
  }
  function rowMarkup(item) {
    return '<div class="software-row" style="--app-color:' + (appColors[item.slug] || "#dedede") + '">'
      + '<div class="table-app-cell">' + appIconMarkup(item) + '<div class="table-name-wrap"><h3 class="card-title">' + displayedName(item) + '</h3><p class="card-tagline">' + escapeHtml(item.tagline || "") + '</p></div></div>'
      + '<div class="table-category">' + escapeHtml(item.category || "") + '</div>'
      + '<div class="table-status">' + stageMarkup(item) + '</div>'
      + '<div class="table-platforms">' + escapeHtml((item.platforms || []).join(" · ")) + '</div>'
      + '<div class="table-links">' + referenceLink(item.sourceUrl, "GITHUB") + externalLink(item.downloadUrl, item.kind === "Launcher" ? "RELEASES" : "DOWNLOADS", "primary") + '</div>'
      + '</div>';
  }
  function render() {
    var filtered = getFiltered();
    var toShow = filtered.slice(0, visibleCount);
    resultCount.textContent = filtered.length === allSoftware.length ? filtered.length + " programas" : filtered.length + " de " + allSoftware.length + " programas";
    renderFiltersSummary();
    softwareGrid.classList.toggle("table-view", selectedView === "table");
    if (!filtered.length) {
      softwareGrid.innerHTML = '<div class="empty-state"><div class="empty-symbol" aria-hidden="true">⌕</div><h3>Nenhum aplicativo encontrado</h3><p>Tente outra busca ou remova algum filtro.</p><button type="button" id="empty-clear">Limpar filtros</button></div>';
      loadMoreWrap.hidden = true;
      document.getElementById("empty-clear").addEventListener("click", clearFilters);
      return;
    }
    softwareGrid.innerHTML = selectedView === "table"
      ? '<div class="table-heading"><span>APP</span><span>CATEGORIA</span><span>STATUS</span><span>PLATAFORMAS</span><span>AÇÕES</span></div>' + toShow.map(rowMarkup).join("")
      : toShow.map(function (item) { return cardMarkup(item, allSoftware.indexOf(item)); }).join("");
    wireImageFallbacks();
    loadMoreWrap.hidden = filtered.length <= visibleCount;
    if (filtered.length > visibleCount) document.getElementById("load-more").textContent = "Mostrar mais aplicativos (" + (filtered.length - visibleCount) + ") ↓";
  }
  function syncSearch(value) {
    searchInput.value = value;
    filterSearchInput.value = value;
    visibleCount = pageSize;
    render();
  }
  function clearFilters() {
    selectedCategory = "";
    selectedStatus = "all";
    searchInput.value = "";
    filterSearchInput.value = "";
    platformFilter.value = "";
    sortFilter.value = "featured";
    visibleCount = pageSize;
    renderCategories();
    renderStatusTabs();
    render();
  }
  function setCategory(category) {
    selectedCategory = category || "";
    visibleCount = pageSize;
    renderCategories();
    render();
    document.getElementById("catalogo").scrollIntoView({behavior:"smooth",block:"start"});
  }
  function setView(view) {
    selectedView = view === "table" ? "table" : "grid";
    viewGridButton.classList.toggle("active", selectedView === "grid");
    viewTableButton.classList.toggle("active", selectedView === "table");
    viewGridButton.setAttribute("aria-pressed", String(selectedView === "grid"));
    viewTableButton.setAttribute("aria-pressed", String(selectedView === "table"));
    render();
  }
  function showError() {
    softwareGrid.hidden = true;
    loadMoreWrap.hidden = true;
    errorState.hidden = false;
    resultCount.textContent = "Catálogo indisponível";
    statusTabs.innerHTML = "";
  }
  function loadCatalog() {
    var requestId = ++loadSequence;
    errorState.hidden = true;
    softwareGrid.hidden = false;
    softwareGrid.innerHTML = '<div class="loading-state"><span class="loader"></span><p>Preparando a biblioteca…</p></div>';
    fetch("data/software.json", {cache:"no-cache"}).then(function (response) {
      if (!response.ok) throw new Error("Não foi possível carregar data/software.json");
      return response.json();
    }).then(function (items) {
      if (requestId !== loadSequence) return;
      if (!Array.isArray(items) || !items.length || items.some(function (item) { return !item || typeof item !== "object" || !item.slug || !item.name; })) {
        throw new Error("O catálogo está vazio ou em formato inválido");
      }
      allSoftware = items;
      renderCategories();
      renderStatusTabs();
      renderPlatformOptions();
      render();
    }).catch(function (error) {
      if (requestId !== loadSequence) return;
      console.error(error);
      showError();
    });
  }
  document.getElementById("search-form").addEventListener("submit", function (event) {
    event.preventDefault();
    syncSearch(searchInput.value);
    document.getElementById("catalogo").scrollIntoView({behavior:"smooth",block:"start"});
  });
  searchInput.addEventListener("input", function () { syncSearch(searchInput.value); });
  filterSearchInput.addEventListener("input", function () { syncSearch(filterSearchInput.value); });
  platformFilter.addEventListener("change", function () { visibleCount = pageSize; render(); });
  sortFilter.addEventListener("change", function () { visibleCount = pageSize; render(); });
  categoryChips.addEventListener("click", function (event) {
    var button = event.target.closest("button[data-category]");
    if (button) setCategory(button.getAttribute("data-category"));
  });
  statusTabs.addEventListener("click", function (event) {
    var button = event.target.closest("button[data-status]");
    if (!button) return;
    selectedStatus = button.getAttribute("data-status");
    visibleCount = pageSize;
    renderStatusTabs();
    render();
  });
  viewGridButton.addEventListener("click", function () { setView("grid"); });
  viewTableButton.addEventListener("click", function () { setView("table"); });
  reloadButton.addEventListener("click", loadCatalog);
  document.getElementById("clear-filters").addEventListener("click", clearFilters);
  document.getElementById("load-more").addEventListener("click", function () { visibleCount += pageSize; render(); });
  document.getElementById("retry-load").addEventListener("click", loadCatalog);
  document.getElementById("current-year").textContent = String(new Date().getFullYear());
  loadCatalog();
}());
