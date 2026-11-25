<?php
/**
 * International-patient + answer-engine block for a service page.
 *
 * Usage, immediately before the closing </main> or the final CTA:
 *   <?php $page_slug = 'knee-replacement'; include "components/international-patients-block.php"; ?>
 *
 * Structure is deliberate. Answer engines (AI Overviews, ChatGPT, Perplexity)
 * extract self-contained passages, so this block leads with one quotable
 * paragraph that answers the head query without needing the rest of the page,
 * then follows with a comparison table and a Q&A list — the three formats
 * those systems cite most often.
 *
 * The FAQ rendered here is the same array that service-schema.php marks up, so
 * the visible text and the structured data can never drift apart. Google
 * requires that match; FAQ markup whose answers are not on the page is a
 * structured-data violation.
 */

require_once __DIR__ . '/seo-config.php';

$cfg = seo_page($page_slug ?? '');

if ($cfg):

$e = fn($s) => htmlspecialchars($s, ENT_QUOTES, 'UTF-8');
?>

<!-- ============ Direct answer + international patients ============ -->
<section class="py-16 bg-white" id="international-patients">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <!-- Quotable answer passage. Kept short, self-contained and factual so
             it can be lifted verbatim by an answer engine. -->
        <div class="max-w-3xl mx-auto mb-14">
            <p class="text-sm font-semibold tracking-widest uppercase text-[#1E97D9] mb-3">
                <?= $e($cfg['label']) ?>
            </p>
            <p class="text-xl md:text-2xl leading-relaxed text-gray-800 border-l-4 border-[#1E97D9] pl-6">
                <?= $e($cfg['answer']) ?>
            </p>
        </div>

        <?php if (!empty($cfg['cost'])): $c = $cfg['cost']; ?>
        <!-- Cost comparison. The single highest-intent query type in medical
             travel, and the format answer engines cite most readily. -->
        <div class="max-w-4xl mx-auto mb-16">
            <h2 class="text-3xl font-bold text-gray-900 mb-3">
                <?= $e($cfg['entity']) ?> Cost: India vs Other Countries
            </h2>
            <p class="text-gray-600 mb-6">
                Indicative all-inclusive ranges in US dollars, covering surgery, implant, hospital
                stay and inpatient physiotherapy. Your own quote is confirmed in writing after the
                surgeon reviews your scans, and is fixed before you travel.
            </p>

            <div class="overflow-x-auto rounded-xl border border-gray-200">
                <table class="w-full text-left border-collapse">
                    <caption class="sr-only">
                        Cost of <?= $e($cfg['entity']) ?> by country, in US dollars
                    </caption>
                    <thead>
                        <tr class="bg-gray-50 border-b border-gray-200">
                            <th scope="col" class="px-5 py-3 text-sm font-semibold text-gray-700">Country</th>
                            <th scope="col" class="px-5 py-3 text-sm font-semibold text-gray-700">Typical cost (USD)</th>
                            <th scope="col" class="px-5 py-3 text-sm font-semibold text-gray-700">Waiting time</th>
                        </tr>
                    </thead>
                    <tbody class="text-gray-700">
                        <tr class="bg-blue-50/60 border-b border-gray-200">
                            <th scope="row" class="px-5 py-4 font-semibold text-[#1E97D9] text-left">
                                India — Impact Ortho Centre
                            </th>
                            <td class="px-5 py-4 font-semibold tabular-nums">
                                $<?= number_format($c['low']) ?> – $<?= number_format($c['high']) ?>
                            </td>
                            <td class="px-5 py-4">No waiting list</td>
                        </tr>
                        <?php foreach ([
                            ['United States', $c['us'] ?? null, 'Varies by insurer'],
                            ['United Kingdom', $c['uk'] ?? null, 'Months on NHS waiting lists'],
                            ['United Arab Emirates', $c['ae'] ?? null, 'Varies by provider'],
                        ] as [$country, $price, $wait]): if (!$price) continue; ?>
                        <tr class="border-b border-gray-200 last:border-0">
                            <th scope="row" class="px-5 py-4 font-medium text-left"><?= $e($country) ?></th>
                            <td class="px-5 py-4 tabular-nums">$<?= number_format($price) ?>+</td>
                            <td class="px-5 py-4"><?= $e($wait) ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>
            <p class="text-xs text-gray-500 mt-3">
                Comparison figures are typical published self-pay ranges and are provided for
                orientation only. They are not quotations from those providers.
            </p>
        </div>
        <?php endif; ?>

        <!-- What international patients actually receive -->
        <div class="max-w-5xl mx-auto mb-16">
            <h2 class="text-3xl font-bold text-gray-900 mb-3">
                <?= $e($cfg['entity']) ?> for International Patients
            </h2>
            <p class="text-gray-600 mb-8 max-w-3xl">
                Impact Ortho Centre has treated patients from over <?= (int) $ORG['countries'] ?> countries.
                Everything below is arranged by the hospital, not by an agency, and is
                included in your treatment coordination at no separate charge.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <?php foreach ($INTL_SERVICES as [$title, $desc]): ?>
                <div class="border border-gray-200 rounded-xl p-6">
                    <h3 class="font-semibold text-gray-900 mb-2"><?= $e($title) ?></h3>
                    <p class="text-gray-600 text-sm leading-relaxed"><?= $e($desc) ?></p>
                </div>
                <?php endforeach; ?>
            </div>
        </div>

        <!-- The journey, as an ordered list because the order is real -->
        <div class="max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">
                How Treatment Works If You Are Travelling From Abroad
            </h2>
            <ol class="space-y-5">
                <?php foreach ($INTL_JOURNEY as $i => [$title, $desc]): ?>
                <li class="flex gap-5">
                    <span class="flex-shrink-0 w-9 h-9 rounded-full bg-[#1E97D9] text-white font-semibold
                                 flex items-center justify-center text-sm"><?= $i + 1 ?></span>
                    <div>
                        <h3 class="font-semibold text-gray-900"><?= $e($title) ?></h3>
                        <p class="text-gray-600 text-sm leading-relaxed"><?= $e($desc) ?></p>
                    </div>
                </li>
                <?php endforeach; ?>
            </ol>
        </div>

        <?php if (!empty($cfg['faqs'])): ?>
        <!-- FAQ. Same array that service-schema.php marks up as FAQPage. -->
        <div class="max-w-3xl mx-auto">
            <h2 class="text-3xl font-bold text-gray-900 mb-8">
                <?= $e($cfg['entity']) ?>: Frequently Asked Questions
            </h2>
            <div class="divide-y divide-gray-200 border-t border-gray-200">
                <?php foreach ($cfg['faqs'] as [$q, $a]): ?>
                <div class="py-6">
                    <h3 class="font-semibold text-lg text-gray-900 mb-2"><?= $e($q) ?></h3>
                    <p class="text-gray-600 leading-relaxed"><?= $e($a) ?></p>
                </div>
                <?php endforeach; ?>
            </div>
        </div>
        <?php endif; ?>

        <!-- Reviewed-by line. Explicit authorship is the strongest single
             E-E-A-T signal available on medical content. -->
        <div class="max-w-3xl mx-auto mt-14 pt-6 border-t border-gray-200">
            <p class="text-sm text-gray-600">
                Medically reviewed by
                <a href="doctor-detail" class="font-semibold text-[#1E97D9] hover:underline"><?= $e($SURGEON['name']) ?></a>,
                <?= $e($SURGEON['jobTitle']) ?>.
                <?= $e(implode(', ', $SURGEON['degrees'])) ?>.
                <?= (int) $SURGEON['experience'] ?> years of experience and over
                <?= number_format($SURGEON['surgeries']) ?> joint replacement surgeries.
            </p>
        </div>

    </div>
</section>

<?php endif; ?>
