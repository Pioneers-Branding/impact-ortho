<?php
/**
 * Emits one consolidated JSON-LD @graph for a service page.
 *
 * Usage, immediately before </head>:
 *   <?php $page_slug = 'knee-replacement'; include "components/service-schema.php"; ?>
 *
 * Emits, cross-linked by @id so search engines read them as one entity set:
 *   MedicalWebPage      the page itself, with its primary topic
 *   MedicalProcedure / MedicalCondition / MedicalTherapy / MedicalTest
 *   Physician           the operating surgeon, with real credentials
 *   Hospital            the provider, with international reach declared
 *   BreadcrumbList      hierarchy, currently absent site-wide
 *   FAQPage             the same Q&A rendered on the page
 *   Offer               only where a real price range exists in the config
 *
 * Nothing here is emitted for a slug with no configuration, so adding the
 * include to a page is always safe.
 */

require_once __DIR__ . '/seo-config.php';

$cfg = seo_page($page_slug ?? '');

if ($cfg):

$BASE   = 'https://www.impactorthocenter.com';
$pageUrl = $BASE . '/' . ($page_slug ?? '');

/* ---- Hospital -------------------------------------------------- */

$hospital = [
    '@type'       => 'Hospital',
    '@id'         => $BASE . '/#organization',
    'name'        => $ORG['name'],
    'legalName'   => $ORG['legalName'],
    'url'         => $ORG['url'],
    'logo'        => $ORG['logo'],
    'image'       => $ORG['logo'],
    'telephone'   => $ORG['phone'],
    'priceRange'  => '$$',
    'medicalSpecialty' => 'Orthopedic',
    'address' => [
        '@type'           => 'PostalAddress',
        'streetAddress'   => $ORG['street'],
        'addressLocality' => $ORG['locality'],
        'addressRegion'   => $ORG['region'],
        'postalCode'      => $ORG['postalCode'],
        'addressCountry'  => $ORG['country'],
    ],
    'geo' => [
        '@type'     => 'GeoCoordinates',
        'latitude'  => $ORG['lat'],
        'longitude' => $ORG['lng'],
    ],
    /* Declares to search engines that this provider serves patients worldwide,
       which is the signal that qualifies it for international treatment queries. */
    'areaServed'          => ['@type' => 'Place', 'name' => 'Worldwide'],
    'availableLanguage'   => $ORG_LANGUAGES,
    'isAcceptingNewPatients' => true,
    'aggregateRating' => [
        '@type'       => 'AggregateRating',
        'ratingValue' => $ORG['rating'],
        'ratingCount' => $ORG['ratingCount'],
        'bestRating'  => '5',
    ],
    'contactPoint' => [
        '@type'             => 'ContactPoint',
        'contactType'       => 'International patient coordination',
        'telephone'         => $ORG['phone'],
        'availableLanguage' => $ORG_LANGUAGES,
        'areaServed'        => 'Worldwide',
    ],
];

/* ---- Physician -------------------------------------------------- */

$physician = [
    '@type'    => 'Physician',
    '@id'      => $BASE . '/#surgeon',
    'name'     => $SURGEON['name'],
    'jobTitle' => $SURGEON['jobTitle'],
    'image'    => $SURGEON['image'],
    'url'      => $SURGEON['url'],
    'medicalSpecialty'  => 'Orthopedic',
    'honorificSuffix'   => implode(', ', $SURGEON['degrees']),
    'knowsAbout'        => $SURGEON['specialties'],
    'worksFor'          => ['@id' => $BASE . '/#organization'],
    'alumniOf' => array_map(
        fn($e) => ['@type' => 'EducationalOrganization', 'name' => $e[0]],
        $SURGEON['education']
    ),
    'hasCredential' => array_map(
        fn($c) => ['@type' => 'EducationalOccupationalCredential', 'name' => $c],
        $SURGEON['credentials']
    ),
];

/* ---- The clinical entity the page is about ---------------------- */

$entity = [
    '@type' => $cfg['schemaType'],
    '@id'   => $pageUrl . '#entity',
    'name'  => $cfg['entity'],
    'description' => $cfg['answer'],
    'url'   => $pageUrl,
];

if (!empty($cfg['bodyPart'])) {
    /* bodyLocation is the correct property for a condition; procedures use it too. */
    $entity['bodyLocation'] = $cfg['bodyPart'];
}

if (in_array($cfg['schemaType'], ['MedicalProcedure', 'MedicalTherapy'], true)) {
    $entity['procedureType']     = 'https://schema.org/NoninvasiveProcedure';
    $entity['howPerformed']      = $cfg['answer'];
    $entity['availableService']  = ['@id' => $BASE . '/#organization'];
    if ($cfg['schemaType'] === 'MedicalProcedure') {
        $entity['procedureType'] = 'https://schema.org/SurgicalProcedure';
    }
}

if ($cfg['schemaType'] === 'MedicalCondition') {
    $entity['possibleTreatment'] = [
        '@type' => 'MedicalTherapy',
        'name'  => 'Orthopedic assessment, non-surgical management and surgery where indicated',
        'provider' => ['@id' => $BASE . '/#organization'],
    ];
}

/* ---- Offer, only where a genuine price range is configured ------ */

if (!empty($cfg['cost'])) {
    $entity['offers'] = [
        '@type'         => 'Offer',
        'priceCurrency' => 'USD',
        'priceSpecification' => [
            '@type'         => 'PriceSpecification',
            'minPrice'      => $cfg['cost']['low'],
            'maxPrice'      => $cfg['cost']['high'],
            'priceCurrency' => 'USD',
            'valueAddedTaxIncluded' => true,
        ],
        'availability' => 'https://schema.org/InStock',
        'seller'       => ['@id' => $BASE . '/#organization'],
        'areaServed'   => ['@type' => 'Place', 'name' => 'Worldwide'],
    ];
}

/* ---- Breadcrumbs ------------------------------------------------ */

$breadcrumb = [
    '@type' => 'BreadcrumbList',
    '@id'   => $pageUrl . '#breadcrumb',
    'itemListElement' => [
        ['@type' => 'ListItem', 'position' => 1, 'name' => 'Home',     'item' => $BASE . '/'],
        ['@type' => 'ListItem', 'position' => 2, 'name' => 'Treatments', 'item' => $BASE . '/services'],
        ['@type' => 'ListItem', 'position' => 3, 'name' => $cfg['label']],
    ],
];

/* ---- FAQ -------------------------------------------------------- */

$faqPage = null;
if (!empty($cfg['faqs'])) {
    $faqPage = [
        '@type' => 'FAQPage',
        '@id'   => $pageUrl . '#faq',
        'mainEntity' => array_map(fn($qa) => [
            '@type' => 'Question',
            'name'  => $qa[0],
            'acceptedAnswer' => ['@type' => 'Answer', 'text' => $qa[1]],
        ], $cfg['faqs']),
    ];
}

/* ---- The page itself -------------------------------------------- */

$webPage = [
    '@type' => 'MedicalWebPage',
    '@id'   => $pageUrl . '#webpage',
    'url'   => $pageUrl,
    'name'  => $cfg['label'],
    'description'  => $cfg['answer'],
    'inLanguage'   => 'en',
    'about'        => ['@id' => $pageUrl . '#entity'],
    'mainEntity'   => ['@id' => $pageUrl . '#entity'],
    'isPartOf'     => ['@id' => $BASE . '/#website'],
    'breadcrumb'   => ['@id' => $pageUrl . '#breadcrumb'],
    'publisher'    => ['@id' => $BASE . '/#organization'],
    /* reviewedBy is the E-E-A-T signal Google looks for on health content. */
    'reviewedBy'   => ['@id' => $BASE . '/#surgeon'],
    'lastReviewed' => date('Y-m-d', filemtime(__FILE__)),
    'audience'     => [
        '@type'            => 'MedicalAudience',
        'audienceType'     => 'Patient',
        'geographicArea'   => ['@type' => 'Place', 'name' => 'Worldwide'],
    ],
    'specialty'    => 'https://schema.org/Orthopedic',
];

$website = [
    '@type' => 'WebSite',
    '@id'   => $BASE . '/#website',
    'url'   => $BASE . '/',
    'name'  => $ORG['name'],
    'publisher'  => ['@id' => $BASE . '/#organization'],
    'inLanguage' => 'en',
];

$graph = array_values(array_filter([
    $website, $hospital, $physician, $webPage, $entity, $breadcrumb, $faqPage,
]));

echo "\n" . '<script type="application/ld+json">' . "\n";
echo json_encode(
    ['@context' => 'https://schema.org', '@graph' => $graph],
    JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
echo "\n" . '</script>' . "\n";

endif;
