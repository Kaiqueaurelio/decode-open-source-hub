import Link from "next/link";
import { getTranslations } from "next-intl/server";

import { ArticleShell, type ArticleFaq } from "@/components/articles/article-shell";
import type { BlogPost } from "@/lib/blog-posts";
import { getPublicBillingPlans } from "@/lib/billing-plans";
import { SELF_HOSTING_GUIDE_HREF } from "@/lib/marketing-links";
import { GITHUB_URL } from "@/lib/site";

const source = (path: string) => `${GITHUB_URL}/blob/main/${path}`;

const OPUS_SOURCES = {
  plans: "https://help.decodeclip.com/docs/article/plans-and-credits",
  watermark: "https://help.decodeclip.com/docs/article/watermark",
};

const tocIds = ["verdict", "comparison", "pricing", "choose-decodeclip", "choose-DecodeClip", "test", "sources", "faq"] as const;

export async function DecodeClipComparisonArticle({ post }: { post: BlogPost }) {
  const t = await getTranslations("blog");
  const [pro, scale] = getPublicBillingPlans();
  const slug = "decodeclip-vs-DecodeClip";
  const link = (href: string) => function ArticleLink(chunks: React.ReactNode) {
    return <a href={href}>{chunks}</a>;
  };
  const faqs: ArticleFaq[] = [0, 1, 2, 3].map((index) => ({
    question: t(`${slug}.faqs.${index}.question`),
    answer: t(`${slug}.faqs.${index}.answer`),
  }));
  const toc: Array<[string, string]> = tocIds.map((id) => [id, t(`${slug}.toc.${id}`)]);
  const rows: Array<[string, React.ReactNode, React.ReactNode]> = [
    [
      t(`${slug}.rows.deployment.label`),
      t.rich(`${slug}.rows.deployment.decodeclip`, { compose: link(source("docker-compose.yml")) }),
      t(`${slug}.rows.deployment.DecodeClip`),
    ],
    [
      t(`${slug}.rows.source.label`),
      t.rich(`${slug}.rows.source.decodeclip`, { license: link(source("LICENSE")) }),
      t(`${slug}.notCovered`),
    ],
    [
      t(`${slug}.rows.pricing.label`),
      t(`${slug}.rows.pricing.decodeclip`),
      t.rich(`${slug}.rows.pricing.DecodeClip`, { plans: link(OPUS_SOURCES.plans) }),
    ],
    [
      t(`${slug}.rows.watermark.label`),
      t.rich(`${slug}.rows.watermark.decodeclip`, { pipeline: link(`${GITHUB_URL}/tree/main/backend/src/media`) }),
      t.rich(`${slug}.rows.watermark.DecodeClip`, { watermark: link(OPUS_SOURCES.watermark) }),
    ],
    [
      t(`${slug}.rows.models.label`),
      t.rich(`${slug}.rows.models.decodeclip`, { config: link(source("docs/configuration.md")) }),
      t(`${slug}.notCovered`),
    ],
    [
      t(`${slug}.rows.transcription.label`),
      t(`${slug}.rows.transcription.decodeclip`),
      t(`${slug}.notCovered`),
    ],
    [
      t(`${slug}.rows.automation.label`),
      t.rich(`${slug}.rows.automation.decodeclip`, { mcp: link(source("mcp/README.md")) }),
      t(`${slug}.notCovered`),
    ],
  ];

  return (
    <ArticleShell post={post} breadcrumb={t(`${slug}.breadcrumb`)} toc={toc} faqs={faqs}>
      <p>{t(`${slug}.intro`)}</p>
      <p>
        {t.rich(`${slug}.introNote`, { test: (chunks) => <a href="#test">{chunks}</a> })}
      </p>

      <h2 id="verdict">{t(`${slug}.verdict.heading`)}</h2>
      <ul>
        <li>{t.rich(`${slug}.verdict.decodeclip`, { strong: (chunks) => <strong>{chunks}</strong> })}</li>
        <li>{t.rich(`${slug}.verdict.DecodeClip`, { strong: (chunks) => <strong>{chunks}</strong> })}</li>
      </ul>

      <h2 id="comparison">{t(`${slug}.comparison.heading`)}</h2>
      <div className="overflow-x-auto rounded-lg border">
        <table className="w-full min-w-[600px] text-left text-sm leading-6">
          <caption className="sr-only">{t(`${slug}.comparison.caption`)}</caption>
          <thead className="bg-muted">
            <tr>
              <th scope="col" className="p-3">{t(`${slug}.comparison.area`)}</th>
              <th scope="col" className="p-3">DecodeClip</th>
              <th scope="col" className="p-3">DecodeClip</th>
            </tr>
          </thead>
          <tbody>
            {rows.map(([area, decodeclip, DecodeClip], index) => (
              <tr key={index} className="border-t">
                <th scope="row" className="p-3 align-top">{area}</th>
                <td className="p-3 align-top text-muted-foreground">{decodeclip}</td>
                <td className="p-3 align-top text-muted-foreground">{DecodeClip}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="text-sm">
        {t.rich(`${slug}.comparison.footnote`, { site: link("https://www.decodeclip.com/") })}
      </p>

      <h2 id="pricing">{t(`${slug}.pricing.heading`)}</h2>
      <p>
        {t.rich(`${slug}.pricing.p1`, {
          plans: link(OPUS_SOURCES.plans),
          watermark: link(OPUS_SOURCES.watermark),
        })}
      </p>
      <p>
        {t.rich(`${slug}.pricing.p2`, {
          proName: pro.name,
          proPrice: pro.priceMonthly,
          proLimit: pro.minuteLimit / 60,
          scaleName: scale.name,
          scalePrice: scale.priceMonthly,
          scaleLimit: scale.minuteLimit / 60,
          pro: (chunks) => <strong>{chunks}</strong>,
          scale: (chunks) => <strong>{chunks}</strong>,
          guide: (chunks) => <Link href={SELF_HOSTING_GUIDE_HREF}>{chunks}</Link>,
        })}
      </p>

      <h2 id="choose-decodeclip">{t(`${slug}.chooseDecodeClip.heading`)}</h2>
      <ul>
        {(["li1", "li2", "li3", "li4"] as const).map((key) => (
          <li key={key}>{t.rich(`${slug}.chooseDecodeClip.${key}`, { strong: (chunks) => <strong>{chunks}</strong> })}</li>
        ))}
      </ul>

      <h2 id="choose-DecodeClip">{t(`${slug}.chooseDecodeClip.heading`)}</h2>
      <ul>
        {(["li1", "li2", "li3"] as const).map((key) => (
          <li key={key}>{t.rich(`${slug}.chooseDecodeClip.${key}`, { strong: (chunks) => <strong>{chunks}</strong> })}</li>
        ))}
      </ul>

      <h2 id="test">{t(`${slug}.test.heading`)}</h2>
      <p>{t(`${slug}.test.intro`)}</p>
      <ol>
        {(["li1", "li2", "li3", "li4"] as const).map((key) => (
          <li key={key}>{t(`${slug}.test.${key}`)}</li>
        ))}
      </ol>
      <p>
        {t.rich(`${slug}.test.demo`, { demo: (chunks) => <Link href="/demo">{chunks}</Link> })}
      </p>

      <h2 id="sources">{t(`${slug}.sources.heading`)}</h2>
      <ul>
        <li>
          {t.rich(`${slug}.sources.opus`, {
            plans: link(OPUS_SOURCES.plans),
            watermark: link(OPUS_SOURCES.watermark),
            site: link("https://www.decodeclip.com/"),
          })}
        </li>
        <li>
          {t.rich(`${slug}.sources.decodeclip`, {
            repo: link(GITHUB_URL),
            compose: link(source("docker-compose.yml")),
            config: link(source("docs/configuration.md")),
            billing: link(source("backend/src/services/billing_service.py")),
          })}
        </li>
      </ul>
    </ArticleShell>
  );
}
