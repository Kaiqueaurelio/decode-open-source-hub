(function () {
  "use strict";
  var allSoftware = [];
  var selectedCategory = "";
  var visibleCount = 12;
  var pageSize = 12;
  var searchInput = document.getElementById("search-input");
  var filterSearchInput = document.getElementById("filter-search-input");
  var platformFilter = document.getElementById("platform-filter");
  var sortFilter = document.getElementById("sort-filter");
  var categoryChips = document.getElementById("category-chips");
  var softwareGrid = document.getElementById("software-grid");
  var resultCount = document.getElementById("result-count");
  var activeFilters = document.getElementById("active-filters");
  var loadMoreWrap = document.getElementById("load-more-wrap");
  var errorState = document.getElementById("error-state");

  function escapeHtml(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (char) {
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char];
    });
  }
  function safeUrl(value) {
    try { var parsed = new URL(value); return parsed.protocol === "https:" ? parsed.href : ""; }
    catch (error) { return ""; }
  }
  function externalLink(value, label, extraClass) {
    var url = safeUrl(value);
    if (!url) return "";
    return '<a class="card-action ' + extraClass + '" href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + ' <span aria-hidden="true">↗</span></a>';
  }
  function getCategories() {
    var counts = {};
    allSoftware.forEach(function (item) { counts[item.category] = (counts[item.category] || 0) + 1; });
    return Object.keys(counts).sort(function (a, b) { return a.localeCompare(b, "pt-BR"); }).map(function (name) { return {name:name,count:counts[name]}; });
  }
  function renderCategories() {
    var categories = getCategories();
    var html = '<button class="category-chip ' + (selectedCategory === "" ? "active" : "") + '" type="button" data-category="">Todas as categorias <span class="chip-count">' + allSoftware.length + '</span></button>';
    categories.forEach(function (category) {
      html += '<button class="category-chip ' + (selectedCategory === category.name ? "active" : "") + '" type="button" data-category="' + escapeHtml(category.name) + '">' + escapeHtml(category.name) + '<span class="chip-count">' + category.count + '</span></button>';
    });
    categoryChips.innerHTML = html;
    document.getElementById("stat-total").textContent = String(allSoftware.length);
    document.getElementById("stat-categories").textContent = String(categories.length);
  }
  function renderPlatformOptions() {
    var platforms = [];
    allSoftware.forEach(function (item) { (item.platforms || []).forEach(function (platform) { if (platforms.indexOf(platform) === -1) platforms.push(platform); }); });
    platforms.sort(function (a, b) { return a.localeCompare(b, "pt-BR"); });
    platformFilter.innerHTML = '<option value="">Todas</option>' + platforms.map(function (platform) { return '<option value="' + escapeHtml(platform) + '">' + escapeHtml(platform) + '</option>'; }).join("");
  }
  function currentSearch() { return (filterSearchInput.value || searchInput.value || "").trim().toLocaleLowerCase("pt-BR"); }
  function getFiltered() {
    var term = currentSearch(), platform = platformFilter.value;
    var found = allSoftware.filter(function (item) {
      var searchable = [item.name,item.tagline,item.description,item.category,item.license].concat(item.tags || []).join(" ").toLocaleLowerCase("pt-BR");
      return (!term || searchable.indexOf(term) !== -1) && (!selectedCategory || item.category === selectedCategory) && (!platform || (item.platforms || []).indexOf(platform) !== -1);
    });
    var sort = sortFilter.value;
    found.sort(function (a,b) {
      if (sort === "name") return a.name.localeCompare(b.name,"pt-BR");
      if (sort === "category") { var cat = a.category.localeCompare(b.category,"pt-BR"); return cat || a.name.localeCompare(b.name,"pt-BR"); }
      return Number(Boolean(b.featured)) - Number(Boolean(a.featured)) || a.name.localeCompare(b.name,"pt-BR");
    });
    return found;
  }
  function renderFiltersSummary() {
    var labels = [];
    if (selectedCategory) labels.push(selectedCategory);
    if (platformFilter.value) labels.push(platformFilter.value);
    if (currentSearch()) labels.push("Busca: " + currentSearch());
    activeFilters.innerHTML = labels.map(function (label) { return '<span class="active-filter">' + escapeHtml(label) + '</span>'; }).join("");
  }
  function cardMarkup(item) {
    var platforms = (item.platforms || []).slice(0,4).map(function (platform) { return '<span class="platform-pill">' + escapeHtml(platform) + '</span>'; }).join("");
    var extra = (item.platforms || []).length > 4 ? '<span class="platform-pill">+' + ((item.platforms || []).length - 4) + '</span>' : "";
    var download = externalLink(item.downloadUrl,"Download","primary");
    var official = externalLink(item.websiteUrl,"Site oficial","secondary");
    var source = externalLink(item.sourceUrl,"Código-fonte","secondary");
    var licenseUrl = safeUrl(item.licenseUrl);
    var licenseMarkup = licenseUrl
      ? '<a class="license-value" href="' + escapeHtml(licenseUrl) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(item.license) + ' ↗</a>'
      : '<span class="license-value">' + escapeHtml(item.license) + '</span>';
    var featured = item.featured ? '<span class="featured-badge">✦ Em destaque</span>' : "";
    return '<article class="software-card"><div class="card-top"><div class="app-icon" aria-hidden="true">' + escapeHtml(item.icon || "◈") + '</div>' + featured + '</div>' +
      '<div class="card-category">' + escapeHtml(item.category) + '</div><div class="card-title-row"><h3 class="card-title">' + escapeHtml(item.name) + '</h3></div>' +
      '<p class="card-tagline">' + escapeHtml(item.tagline) + '</p><p class="card-description">' + escapeHtml(item.description) + '</p>' +
      '<div class="platform-row" aria-label="Plataformas: ' + escapeHtml((item.platforms || []).join(", ")) + '">' + platforms + extra + '</div>' +
      '<div class="license-row"><span class="license-label">Licença</span>' + licenseMarkup + '</div>' +
      '<div class="card-actions">' + download + official + source + '</div></article>';
  }
  function render() {
    var filtered = getFiltered(), toShow = filtered.slice(0,visibleCount);
    resultCount.textContent = filtered.length === allSoftware.length ? filtered.length + " programas" : filtered.length + " de " + allSoftware.length + " programas";
    renderFiltersSummary();
    if (!filtered.length) {
      softwareGrid.innerHTML = '<div class="empty-state"><div class="empty-symbol" aria-hidden="true">⌕</div><h3>Nenhum programa encontrado</h3><p>Tente outro termo ou remova algum filtro.</p><button type="button" id="empty-clear">Limpar pesquisa e filtros</button></div>';
      loadMoreWrap.hidden = true;
      document.getElementById("empty-clear").addEventListener("click",clearFilters);
      return;
    }
    softwareGrid.innerHTML = toShow.map(cardMarkup).join("");
    loadMoreWrap.hidden = filtered.length <= visibleCount;
    if (filtered.length > visibleCount) document.getElementById("load-more").textContent = "Mostrar mais programas (" + (filtered.length - visibleCount) + " restantes) ↓";
  }
  function syncSearch(value) { searchInput.value = value; filterSearchInput.value = value; visibleCount = pageSize; render(); }
  function clearFilters() {
    selectedCategory = ""; searchInput.value = ""; filterSearchInput.value = ""; platformFilter.value = ""; sortFilter.value = "featured"; visibleCount = pageSize; renderCategories(); render();
  }
  function setCategory(category) {
    selectedCategory = category || ""; visibleCount = pageSize; renderCategories(); render();
    document.getElementById("catalogo").scrollIntoView({behavior:"smooth",block:"start"});
  }
  function showError() { softwareGrid.hidden = true; loadMoreWrap.hidden = true; errorState.hidden = false; resultCount.textContent = "Catálogo indisponível"; }
  function loadCatalog() {
    errorState.hidden = true; softwareGrid.hidden = false;
    softwareGrid.innerHTML = '<div class="loading-state"><span class="loader"></span><p>Preparando a biblioteca…</p></div>';
    fetch("data/software.json",{cache:"no-cache"}).then(function (response) {
      if (!response.ok) throw new Error("Não foi possível carregar data/software.json");
      return response.json();
    }).then(function (items) {
      if (!Array.isArray(items) || !items.length) throw new Error("O catálogo está vazio ou em formato inválido");
      allSoftware = items; renderCategories(); renderPlatformOptions(); render();
    }).catch(function (error) { console.error(error); showError(); });
  }
  document.getElementById("search-form").addEventListener("submit",function (event) { event.preventDefault(); syncSearch(searchInput.value); document.getElementById("catalogo").scrollIntoView({behavior:"smooth",block:"start"}); });
  searchInput.addEventListener("input",function () { syncSearch(searchInput.value); });
  filterSearchInput.addEventListener("input",function () { syncSearch(filterSearchInput.value); });
  platformFilter.addEventListener("change",function () { visibleCount = pageSize; render(); });
  sortFilter.addEventListener("change",function () { visibleCount = pageSize; render(); });
  categoryChips.addEventListener("click",function (event) { var button = event.target.closest("button[data-category]"); if (button) setCategory(button.getAttribute("data-category")); });
  document.getElementById("clear-filters").addEventListener("click",clearFilters);
  document.getElementById("load-more").addEventListener("click",function () { visibleCount += pageSize; render(); });
  document.getElementById("retry-load").addEventListener("click",loadCatalog);
  document.getElementById("current-year").textContent = String(new Date().getFullYear());
  loadCatalog();
}());
