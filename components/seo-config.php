<?php
/**
 * Central SEO / schema / international-patient configuration.
 *
 * ONE file drives structured data and the international-patient block on every
 * service page. To change a phone number, a credential, a cost or an FAQ across
 * the whole site, edit it here — not in 2,371 page files.
 *
 * Pages opt in with:  <?php $page_slug = 'back-pain'; ?>  before the includes.
 *
 * COST FIGURES: only fill `cost` where you have a real, current, quotable range.
 * A null cost hides the price row and the Offer schema for that page. Never
 * publish an estimated price on a medical site.
 */

/* ------------------------------------------------------------------ */
/* Organisation-level facts. Single source of truth.                   */
/* ------------------------------------------------------------------ */

$ORG = [
    'name'        => 'Impact Ortho Centre',
    'legalName'   => 'Impact Orthopedic & Joint Replacement Center',
    'url'         => 'https://www.impactorthocenter.com/',
    'logo'        => 'https://impactorthocenter.com/photos/logo-1-impact.webp',
    'phone'       => '+919494559848',
    'street'      => 'Apollo Hospitals, Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar',
    'locality'    => 'Hyderabad',
    'region'      => 'Telangana',
    'regionCode'  => 'IN-TG',
    'postalCode'  => '500033',
    'country'     => 'IN',
    'lat'         => 17.415639,
    'lng'         => 78.413217,
    'foundedYears'=> 24,
    'surgeries'   => 5000,
    'countries'   => 40,
    'rating'      => '4.9',
    'ratingCount' => 5000,
];

/* Languages the coordination team actually supports. Used by schema and by the
   international block. Trim this list if any of them is not genuinely staffed. */
$ORG_LANGUAGES = ['English', 'Hindi', 'Telugu', 'Arabic', 'Bengali', 'Swahili', 'French'];

/* ------------------------------------------------------------------ */
/* Lead surgeon. Feeds Physician schema and E-E-A-T author signals.    */
/* ------------------------------------------------------------------ */

$SURGEON = [
    'name'       => 'Dr. Ratnakar Rao',
    'jobTitle'   => 'Senior Consultant — Robotic Joint Replacement & Arthroscopic Surgeon',
    'image'      => 'https://impactorthocenter.com/photos/dr-ratnakar.webp',
    'url'        => 'https://www.impactorthocenter.com/doctor-detail',
    'experience' => 24,
    'surgeries'  => 5000,
    'degrees'    => ['MBBS', 'MS (Orthopedics)', 'M.Ch (Orthopedics)'],
    'education'  => [
        ['Osmania Medical College, Hyderabad', 'MBBS'],
        ['Gandhi Medical College, Hyderabad', 'MS (Orthopedics)'],
        ['University of Dundee, United Kingdom', 'M.Ch (Orthopedics)'],
    ],
    'credentials' => [
        'Fellowship, Royal College of Surgeons, United Kingdom',
        'Certified Mako Robotic-Arm Assisted Surgeon',
        'Robotic Surgery Certification, United States of America',
    ],
    'specialties' => [
        'Robotic Knee Replacement',
        'Robotic Hip Replacement',
        'Revision Joint Replacement',
        'Arthroscopy and Sports Medicine',
    ],
];

/* ------------------------------------------------------------------ */
/* What international patients get. Rendered and marked up per page.   */
/* ------------------------------------------------------------------ */

$INTL_SERVICES = [
    ['Medical visa assistance',   'Invitation letters issued within 24 hours and guidance through the full medical visa application.'],
    ['Free tele-consultation',    'Send your reports and speak to the operating surgeon before you book any travel.'],
    ['Airport pickup and stay',   'Arrival transfer plus accommodation arranged near the hospital for you and one attendant.'],
    ['Dedicated coordinator',     'One named point of contact for appointments, billing, records and local arrangements.'],
    ['Interpreter support',       'Complimentary interpreters so nothing in your consent or care plan is lost in translation.'],
    ['Remote follow-up',          'Tele-consultations with your own surgeon after you fly home, at no extra charge.'],
];

$INTL_JOURNEY = [
    ['Send your reports',      'Upload X-rays, MRI and prior notes. You get a written opinion and a plan.'],
    ['Free tele-consultation', 'Meet the surgeon who will operate, not a call-centre agent.'],
    ['Visa and travel',        'We issue the invitation letter and help with flights and accommodation.'],
    ['Arrival and workup',     'Airport pickup, pre-operative evaluation and anaesthesia clearance.'],
    ['Surgery and inpatient',  'Your procedure, then 24/7 nursing and daily surgeon review.'],
    ['Rehab and return',       'Supervised physiotherapy, discharge summary, and follow-up after you land home.'],
];

/* ------------------------------------------------------------------ */
/* Per-page configuration.                                             */
/*                                                                     */
/*   schemaType  MedicalCondition | MedicalProcedure | MedicalTherapy   */
/*               | MedicalTest | Physician | MedicalOrganization        */
/*   entity      Exact clinical name of the condition or procedure.     */
/*   bodyPart    Schema.org bodyLocation string, or null.               */
/*   answer      ONE quotable paragraph, 40-60 words, that directly     */
/*               answers the page's head query. This is the passage AI  */
/*               engines lift. Keep it self-contained and factual.      */
/*   cost        ['low'=>int,'high'=>int,'us'=>int,'uk'=>int,'ae'=>int] */
/*               in USD, or null to hide the cost table entirely.       */
/*   faqs        [[question, answer], ...] — rendered AND marked up.    */
/* ------------------------------------------------------------------ */

$SEO_PAGES = [

'knee-replacement' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Knee Replacement Surgery',
    'label'      => 'Knee Replacement Surgery in India',
    'bodyPart'   => 'Knee',
    'answer'     => 'Knee replacement surgery in India costs roughly $4,000 to $8,000 at Impact Ortho Centre in Hyderabad, against $40,000 or more in the United States. Surgery is performed by Dr. Ratnakar Rao, a Mako-certified surgeon with 24 years of experience and over 5,000 joint replacements, with no waiting list for international patients.',
    /* Only 'low', 'high' and 'us' are sourced from Impact Ortho's own published
       FAQ. 'uk' and 'ae' are intentionally null — add them only from a citable
       published figure, never an estimate. Null rows are omitted from the table. */
    'cost'       => ['low' => 4000, 'high' => 8000, 'us' => 40000, 'uk' => null, 'ae' => null],
    'faqs'       => [
        ['How much does knee replacement surgery cost in India?',
         'At Impact Ortho Centre the range is approximately $4,000 to $8,000 depending on implant type and whether one or both knees are treated. The equivalent procedure costs $40,000 or more in the United States. Your written quote is fixed before you travel and covers surgery, implant, hospital stay and inpatient physiotherapy.'],
        ['Is knee replacement in India as safe as in the US or UK?',
         'The implants are the same FDA-approved brands used in Western hospitals, and the procedure is performed with Mako robotic-arm assistance. Dr. Ratnakar Rao holds a Fellowship from the Royal College of Surgeons in the UK, an M.Ch from the University of Dundee, and robotic surgery certification from the United States.'],
        ['How long do I need to stay in India for knee replacement?',
         'Most international patients plan for about three weeks in Hyderabad: two to three days of pre-operative workup, three to five days as an inpatient, and the remainder in supervised outpatient physiotherapy before the surgeon clears you to fly. Your coordinator books accommodation for the full period.'],
        ['Do you help with the medical visa?',
         'Yes. We issue a hospital invitation letter within 24 hours of confirming your treatment plan, which is the document your embassy requires for a medical visa. Impact Ortho Centre has treated patients from over 40 countries and the coordination team handles the paperwork end to end.'],
    ],
],

'robotic-knee-replacement' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Robotic-Arm Assisted Knee Replacement',
    'label'      => 'Robotic Knee Replacement in India',
    'bodyPart'   => 'Knee',
    'answer'     => 'Robotic knee replacement at Impact Ortho Centre uses the Mako robotic-arm system to position the implant to sub-millimetre accuracy from a CT-based plan built for your own anatomy. Dr. Ratnakar Rao was among the first surgeons in India to perform Mako-assisted joint replacement and has completed over 5,000 joint surgeries.',
    'cost'       => null,
    'faqs'       => [
        ['What makes robotic knee replacement different from conventional surgery?',
         'A CT scan of your knee is used to build a three-dimensional surgical plan before the operation. During surgery the Mako robotic arm holds the cutting instrument inside the boundaries of that plan, which allows implant positioning to sub-millimetre accuracy rather than relying on manual jigs and visual alignment.'],
        ['Does a robot perform the surgery?',
         'No. The surgeon performs the operation throughout. The robotic arm is a guidance instrument that constrains where the cutting tool can travel, so it cannot deviate from the plan the surgeon approved. Dr. Ratnakar Rao is a certified Mako robotic surgeon and controls every step.'],
        ['Is robotic knee replacement available to international patients?',
         'Yes. Mako robotic-arm assisted surgery is available to all patients at our Hyderabad centre with no waiting list, and international patients receive visa assistance, airport pickup, interpreter support and remote surgeon follow-up after returning home.'],
    ],
],

'total-hip-replacement' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Total Hip Replacement',
    'label'      => 'Total Hip Replacement Surgery in India',
    'bodyPart'   => 'Hip',
    'answer'     => 'Total hip replacement at Impact Ortho Centre in Hyderabad replaces the damaged hip joint with an implant, performed by a surgeon with 24 years of experience and over 5,000 joint replacements. Robotic-arm assistance is used to optimise implant positioning, and international patients receive visa support and remote follow-up.',
    'cost'       => null,
    'faqs'       => [
        ['Who needs a total hip replacement?',
         'It is usually considered when hip pain from advanced arthritis, avascular necrosis or a severe fracture limits walking and sleep, and no longer responds to medication, injections or physiotherapy. The decision is made after imaging and an examination, not from symptoms alone.'],
        ['Can hip replacement be done with robotic assistance?',
         'Yes. Robotic-arm assistance is used to plan and control implant positioning, which matters in the hip because cup orientation affects stability and wear. Dr. Ratnakar Rao holds robotic surgery certification from the United States and performs both robotic knee and hip replacement.'],
        ['Do you accept international patients for hip replacement?',
         'Yes. Impact Ortho Centre has treated patients from over 40 countries. You start with a free tele-consultation on your existing scans, receive a written plan and a fixed quote, and only then arrange travel. We issue the medical visa invitation letter within 24 hours.'],
    ],
],

'shoulder-replacement' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Total Shoulder Replacement',
    'label'      => 'Total Shoulder Replacement Surgery in India',
    'bodyPart'   => 'Shoulder',
    'answer'     => 'Total shoulder replacement at Impact Ortho Centre replaces the damaged ball and socket of the shoulder to restore pain-free overhead movement. It is offered for advanced shoulder arthritis and irreparable rotator cuff damage, with no waiting list and full travel coordination for international patients.',
    'cost'       => null,
    'faqs'       => [
        ['When is shoulder replacement recommended?',
         'Typically for advanced shoulder arthritis, avascular necrosis of the humeral head, or an irreparable rotator cuff tear where pain persists at rest and at night despite injections and physiotherapy. Imaging and examination determine whether a standard or reverse replacement is appropriate.'],
        ['How long is recovery after shoulder replacement?',
         'You are usually discharged within a few days and begin guided physiotherapy immediately, with movement restrictions for the first several weeks. Your surgeon gives you a written rehabilitation schedule; international patients complete the early supervised phase in Hyderabad before flying home.'],
    ],
],

'arthroscopy' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Arthroscopy',
    'label'      => 'Arthroscopy Surgery in India',
    'bodyPart'   => 'Joint',
    'answer'     => 'Arthroscopy is keyhole joint surgery performed through incisions a few millimetres wide, using a camera to diagnose and repair damage inside the knee, shoulder, hip or ankle. At Impact Ortho Centre it is performed by a surgeon with 24 years of experience in arthroscopic and sports medicine procedures.',
    'cost'       => null,
    'faqs'       => [
        ['What conditions can arthroscopy treat?',
         'Common indications include meniscus tears, cruciate ligament injuries, rotator cuff tears, shoulder impingement, cartilage damage and loose bodies within a joint. It is used both to confirm a diagnosis and to carry out the repair in the same sitting.'],
        ['Is arthroscopy day-care surgery?',
         'Many arthroscopic procedures are performed as day care or with a single overnight stay, because the incisions are small and there is no large muscle dissection. The exact plan depends on the joint, the repair performed and the anaesthetic used.'],
    ],
],

'trauma-surgery' => [
    'schemaType' => 'MedicalProcedure',
    'entity'     => 'Orthopedic Trauma Surgery',
    'label'      => 'Trauma Surgery & Fracture Care in India',
    'bodyPart'   => 'Bone',
    'answer'     => 'Orthopedic trauma surgery at Impact Ortho Centre treats fractures, dislocations and complex bone injuries, including malunion and nonunion cases referred after earlier surgery elsewhere. Care runs from emergency fixation through rehabilitation, supported by on-site imaging and a dedicated physiotherapy team.',
    'cost'       => null,
    'faqs'       => [
        ['Do you treat fractures that failed to heal after previous surgery?',
         'Yes. Nonunion and malunion after earlier fixation are among the referrals we handle, along with revision of failed implants. These cases are assessed with fresh imaging, and the plan is discussed with you in writing before anything is scheduled.'],
        ['Can international patients be treated for an old fracture injury?',
         'Yes. Send your existing X-rays, CT scans and prior operative notes for a free tele-consultation. If surgery is appropriate you receive a written plan and quote, and we issue the medical visa invitation letter within 24 hours of your confirmation.'],
    ],
],

'physiotherapy-rehabilitation' => [
    'schemaType' => 'MedicalTherapy',
    'entity'     => 'Physiotherapy and Rehabilitation',
    'label'      => 'Physiotherapy & Rehabilitation Services in India',
    'bodyPart'   => null,
    'answer'     => 'Impact Ortho Centre provides supervised physiotherapy and rehabilitation both after surgery and as a non-surgical treatment in its own right. International patients complete the early supervised phase in Hyderabad and continue with a written home programme plus tele-consultations after returning home.',
    'cost'       => null,
    'faqs'       => [
        ['Do I need physiotherapy after joint replacement?',
         'Yes. Supervised rehabilitation is what converts a well-positioned implant into restored function, and it begins within a day of most joint replacements. You receive a written schedule covering the supervised phase and the home programme that follows.'],
        ['Can physiotherapy avoid the need for surgery?',
         'For many conditions, including early arthritis, tennis elbow, shoulder impingement and most back and neck pain, structured physiotherapy is the first-line treatment and surgery is considered only if it fails. Your surgeon will tell you plainly which category you are in.'],
    ],
],

'diagnostic-services' => [
    'schemaType' => 'MedicalTest',
    'entity'     => 'Orthopedic Diagnostic Services',
    'label'      => 'Advanced Diagnostic Services in India',
    'bodyPart'   => null,
    'answer'     => 'Impact Ortho Centre provides on-site orthopedic diagnostics including digital X-ray, MRI, CT and bone density scanning, so that assessment, imaging and the surgical decision happen in one place. International patients can have existing scans reviewed remotely before travelling.',
    'cost'       => null,
    'faqs'       => [
        ['Can you review scans done in my own country?',
         'Yes. Upload your X-rays, MRI or CT images and prior reports and the surgeon will review them in a free tele-consultation. Repeat imaging is only requested when the existing study is too old, incomplete, or of insufficient quality to plan surgery.'],
        ['What imaging is needed before joint replacement?',
         'Robotic joint replacement is planned from a CT scan of the affected joint, in addition to standing X-rays. Any additional tests depend on your general health and are confirmed during the pre-operative evaluation.'],
    ],
],

/* ---- Conditions ---- */

'arthritis' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Arthritis',
    'label'      => 'Arthritis Treatment in India',
    'bodyPart'   => 'Joint',
    'answer'     => 'Arthritis treatment at Impact Ortho Centre ranges from medication, injections and supervised physiotherapy through to robotic joint replacement when the joint surface is destroyed. Treatment is chosen from imaging and examination, and international patients can begin with a free tele-consultation on their existing scans.',
    'cost'       => null,
    'faqs'       => [
        ['Does arthritis always end in joint replacement?',
         'No. Most people with arthritis are managed without surgery using medication, injections, weight and activity modification, and structured physiotherapy. Joint replacement is considered when the cartilage surface is largely gone and pain limits sleep and walking despite those measures.'],
        ['Can I be assessed for arthritis treatment from abroad?',
         'Yes. Send your recent X-rays or MRI and a summary of what you have already tried. The surgeon reviews them in a free tele-consultation and tells you whether your arthritis is at a stage where travelling for surgery is worthwhile, or whether it should be managed at home.'],
    ],
],

'avascular-necrosis' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Avascular Necrosis',
    'label'      => 'Avascular Necrosis Treatment in India',
    'bodyPart'   => 'Hip',
    'answer'     => 'Avascular necrosis is the death of bone tissue caused by an interrupted blood supply, most often affecting the hip. Treatment at Impact Ortho Centre depends on the stage: joint-preserving surgery may be possible when it is caught early, while collapsed joints are treated with replacement.',
    'cost'       => null,
    'faqs'       => [
        ['Can avascular necrosis be treated without joint replacement?',
         'In early stages, before the bone surface collapses, joint-preserving options such as core decompression may be possible. Once the femoral head has collapsed, joint replacement is usually the reliable option. Staging on MRI is what separates the two, which is why early imaging matters.'],
        ['How quickly should avascular necrosis be assessed?',
         'Promptly. The treatment options narrow as the disease progresses from a preserved joint surface to a collapsed one, so an MRI early in the course of hip pain, particularly after steroid use or a fracture, changes what can be offered.'],
    ],
],

'osteoporosis' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Osteoporosis',
    'label'      => 'Osteoporosis Treatment in India',
    'bodyPart'   => 'Bone',
    'answer'     => 'Osteoporosis weakens bone until ordinary loads cause fractures, often of the hip, spine or wrist. Impact Ortho Centre assesses it with bone density scanning and treats both the bone loss itself and the fractures that result, including surgical fixation where required.',
    'cost'       => null,
    'faqs'       => [
        ['How is osteoporosis diagnosed?',
         'With a bone mineral density scan, usually DEXA, alongside blood tests to look for treatable causes of bone loss. A fracture from a minor fall is itself a strong indicator and should prompt testing rather than being treated as an isolated injury.'],
        ['Does osteoporosis affect joint replacement surgery?',
         'It can affect implant fixation and the risk of fracture around the implant, so bone quality is assessed before joint replacement and factored into the choice of implant and fixation method.'],
    ],
],

'back-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Back Pain',
    'label'      => 'Back Pain Treatment in India',
    'bodyPart'   => 'Back',
    'answer'     => 'Back pain treatment at Impact Ortho Centre begins with identifying the source, whether muscular, disc-related, nerve compression or referred from the hip. Most cases are treated without surgery using medication, targeted injections and supervised physiotherapy, with imaging used to rule out causes that need intervention.',
    'cost'       => null,
    'faqs'       => [
        ['When does back pain need a scan?',
         'Imaging is warranted when pain follows significant trauma, when it radiates down the leg with numbness or weakness, when it wakes you at night, or when it persists beyond several weeks of appropriate treatment. Routine early scans for simple back pain rarely change what is done.'],
        ['Does back pain usually need surgery?',
         'No. The large majority of back pain is treated without surgery. Surgery is considered mainly for nerve compression causing progressive weakness, or for instability and deformity, and even then only after non-surgical treatment has been given a fair trial.'],
    ],
],

'neck-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Neck Pain',
    'label'      => 'Neck Pain Treatment in India',
    'bodyPart'   => 'Neck',
    'answer'     => 'Neck pain treatment at Impact Ortho Centre covers postural and muscular causes, cervical disc problems and nerve compression. Assessment separates pain that will settle with physiotherapy and posture correction from pain caused by nerve compression, which needs different treatment.',
    'cost'       => null,
    'faqs'       => [
        ['What causes most neck pain?',
         'Sustained poor posture and muscular strain account for the majority, particularly with desk and screen work. Cervical disc degeneration and nerve compression are less common but need to be identified, because they are treated differently and can cause arm symptoms.'],
        ['When is neck pain a warning sign?',
         'Seek assessment promptly if neck pain comes with weakness or numbness in the arms or hands, problems with balance or fine hand movements, or if it follows a significant injury. These suggest nerve or spinal cord involvement rather than simple muscular pain.'],
    ],
],

'knee-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Knee Pain',
    'label'      => 'Knee Pain Treatment in India',
    'bodyPart'   => 'Knee',
    'answer'     => 'Knee pain treatment at Impact Ortho Centre starts by separating mechanical causes such as meniscus and ligament tears from degenerative arthritis, because the treatments differ. Options run from physiotherapy and injections to keyhole arthroscopy and, in advanced arthritis, robotic knee replacement.',
    'cost'       => null,
    'faqs'       => [
        ['What does it mean if my knee locks or gives way?',
         'Locking, catching or giving way usually points to a mechanical problem inside the joint such as a meniscus tear, a loose fragment of cartilage, or ligament instability, rather than to arthritis alone. These are typically assessed with an MRI and are often treatable arthroscopically.'],
        ['Do I need surgery for knee pain?',
         'Most knee pain is treated without surgery. Surgery is considered for mechanical damage that will not heal on its own, such as certain meniscus and ligament tears, or for arthritis that has destroyed the joint surface and no longer responds to other treatment.'],
    ],
],

'shoulder-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Shoulder Pain',
    'label'      => 'Shoulder Pain Treatment in India',
    'bodyPart'   => 'Shoulder',
    'answer'     => 'Shoulder pain treatment at Impact Ortho Centre covers rotator cuff disease, impingement, frozen shoulder, instability and arthritis. Because these present similarly but are treated very differently, assessment combines examination with imaging before any treatment is recommended.',
    'cost'       => null,
    'faqs'       => [
        ['Why does my shoulder hurt more at night?',
         'Night pain that stops you lying on the affected side is characteristic of rotator cuff problems and shoulder impingement, and it is one of the more reliable signs that the shoulder needs assessment rather than rest alone.'],
        ['Is frozen shoulder the same as a rotator cuff tear?',
         'No. Frozen shoulder is a stiffening of the joint capsule that limits movement in every direction, including when someone else moves your arm for you. A rotator cuff tear causes weakness and pain but usually preserves passive movement. The distinction changes the treatment entirely.'],
    ],
],

'rotator-cuff-tear' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Rotator Cuff Tear',
    'label'      => 'Rotator Cuff Tear Treatment in India',
    'bodyPart'   => 'Shoulder',
    'answer'     => 'A rotator cuff tear is a tear in the tendons that stabilise and lift the shoulder, causing weakness and night pain. Impact Ortho Centre treats partial tears with physiotherapy and injections, and repairs full-thickness tears arthroscopically through keyhole incisions.',
    'cost'       => null,
    'faqs'       => [
        ['Can a rotator cuff tear heal without surgery?',
         'Partial tears often improve with a structured physiotherapy programme and activity modification. Full-thickness tears do not heal back together on their own, though not every full-thickness tear requires repair; that depends on your age, function and symptoms.'],
        ['How is a rotator cuff repair performed?',
         'Usually arthroscopically, through several keyhole incisions, with the torn tendon reattached to the bone using anchors. This avoids the larger open exposure and generally allows earlier, more comfortable rehabilitation.'],
    ],
],

'shoulder-impingement' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Shoulder Impingement Syndrome',
    'label'      => 'Shoulder Impingement Treatment in India',
    'bodyPart'   => 'Shoulder',
    'answer'     => 'Shoulder impingement occurs when rotator cuff tendons are compressed as the arm is raised, producing pain through a specific arc of movement. Impact Ortho Centre treats it primarily with targeted physiotherapy and injections, reserving arthroscopic decompression for cases that do not settle.',
    'cost'       => null,
    'faqs'       => [
        ['What does shoulder impingement feel like?',
         'Pain concentrated in a band of movement as you raise the arm to shoulder height, often with a catch, and pain reaching behind your back or overhead. It commonly worsens at night and with repetitive overhead activity.'],
        ['Does shoulder impingement need surgery?',
         'Usually not. A correctly targeted physiotherapy programme resolves most cases, sometimes helped by an injection. Arthroscopic decompression is considered when a properly supervised programme has failed over several months.'],
    ],
],

'tennis-elbow' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Lateral Epicondylitis',
    'label'      => 'Tennis Elbow Treatment in India',
    'bodyPart'   => 'Elbow',
    'answer'     => 'Tennis elbow is a degenerative overuse condition of the tendon on the outer elbow, causing pain when gripping or lifting. Most cases at Impact Ortho Centre are treated non-surgically with load management, a specific eccentric exercise programme, bracing and injections where indicated.',
    'cost'       => null,
    'faqs'       => [
        ['Do I have to play tennis to get tennis elbow?',
         'No. The large majority of cases occur in people who have never played tennis. It results from repetitive gripping and wrist extension, so it is common in manual trades, desk work with poor setup, and any repetitive lifting task.'],
        ['How long does tennis elbow take to settle?',
         'It is typically slow, often several months, and the single most important factor is doing the loading exercises consistently rather than resting completely. Complete rest tends to prolong it. Persistent cases that fail a supervised programme may need further intervention.'],
    ],
],

'elbow-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Elbow Pain',
    'label'      => 'Elbow Pain Treatment in India',
    'bodyPart'   => 'Elbow',
    'answer'     => 'Elbow pain treatment at Impact Ortho Centre covers tendon overuse conditions such as tennis and golfer\'s elbow, nerve compression, arthritis, stiffness and instability after injury. Assessment identifies which structure is involved, because tendon, nerve and joint problems need different treatment.',
    'cost'       => null,
    'faqs'       => [
        ['What causes pain on the inside versus the outside of the elbow?',
         'Pain on the outer side is most often tennis elbow, affecting the tendon that extends the wrist. Pain on the inner side is usually golfer\'s elbow, affecting the flexor tendon, and can coexist with irritation of the ulnar nerve, which causes tingling in the little and ring fingers.'],
        ['Should elbow stiffness after an injury be treated?',
         'Yes, and early. Elbows are prone to losing movement after injury or immobilisation, and stiffness becomes progressively harder to reverse. Prompt supervised rehabilitation gives the best chance of regaining a functional range.'],
    ],
],

'hand-wrist-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Hand and Wrist Pain',
    'label'      => 'Hand & Wrist Pain Treatment in India',
    'bodyPart'   => 'Wrist',
    'answer'     => 'Hand and wrist pain treatment at Impact Ortho Centre covers carpal tunnel syndrome, tendon conditions such as De Quervain\'s and trigger finger, arthritis of the thumb base and wrist, and injuries including scaphoid fractures and ligament tears.',
    'cost'       => null,
    'faqs'       => [
        ['What causes numbness and tingling in the fingers at night?',
         'Night-time numbness and tingling in the thumb, index and middle fingers that makes you shake your hand awake is the classic presentation of carpal tunnel syndrome, caused by compression of the median nerve at the wrist. It is confirmed with a nerve conduction study.'],
        ['Can a wrist fracture be missed on an initial X-ray?',
         'Yes. Scaphoid fractures in particular are frequently invisible on the first X-ray. If there is tenderness in the anatomical snuffbox after a fall on an outstretched hand, the wrist should be treated as fractured and re-imaged, because a missed scaphoid fracture can fail to unite.'],
    ],
],

'foot-ankle-pain' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Foot and Ankle Pain',
    'label'      => 'Foot & Ankle Pain Treatment in India',
    'bodyPart'   => 'Ankle',
    'answer'     => 'Foot and ankle treatment at Impact Ortho Centre covers plantar fasciitis, Achilles tendon problems, ankle instability after repeated sprains, arthritis and fractures. Most conditions are managed without surgery through targeted rehabilitation, orthotics and load modification.',
    'cost'       => null,
    'faqs'       => [
        ['Why does my heel hurt most on the first steps of the morning?',
         'Sharp heel pain on the first steps after waking or after sitting, easing as you walk, is the characteristic pattern of plantar fasciitis. It is usually treated successfully with a calf and plantar fascia stretching programme, footwear changes and orthotics.'],
        ['Do repeated ankle sprains need treatment?',
         'Yes. Repeated sprains suggest the ligaments have healed loose or that the balance reflexes protecting the ankle have not recovered. Untreated instability accelerates cartilage damage, so it is worth addressing with a proprioceptive rehabilitation programme, and surgical stabilisation if that fails.'],
    ],
],

'meniscus-tear' => [
    'schemaType' => 'MedicalCondition',
    'entity'     => 'Meniscus Tear',
    'label'      => 'Meniscus Tear Treatment in India',
    'bodyPart'   => 'Knee',
    'answer'     => 'A meniscus tear is a tear in the cartilage that cushions the knee, causing pain, swelling and sometimes locking. Impact Ortho Centre repairs tears arthroscopically where the tear pattern and blood supply allow, and preserves as much meniscus as possible, because removal accelerates arthritis.',
    'cost'       => null,
    'faqs'       => [
        ['Is a meniscus tear repaired or removed?',
         'Repair is preferred wherever the tear location and blood supply make healing likely, because removing meniscus tissue increases the load on the joint surface and accelerates arthritis. Tears in the poorly vascularised inner zone may not be repairable, in which case only the damaged portion is trimmed.'],
        ['Can a meniscus tear heal without surgery?',
         'Small tears in the outer, well-supplied zone and degenerative tears in older knees often settle with physiotherapy and time. Tears causing true mechanical locking generally need arthroscopic treatment, because the displaced fragment is physically blocking the joint.'],
    ],
],

];

/* Slug aliases: pages that share a config. */
$SEO_ALIASES = [
    'hand-and-wrist-pain'  => 'hand-wrist-pain',
    'total-knee-replacement' => 'knee-replacement',
];

/**
 * Resolve a slug to its configuration, following aliases.
 */
function seo_page(string $slug): ?array
{
    global $SEO_PAGES, $SEO_ALIASES;
    $slug = $SEO_ALIASES[$slug] ?? $slug;
    return $SEO_PAGES[$slug] ?? null;
}
