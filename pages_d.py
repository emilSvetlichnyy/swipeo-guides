from _src import *

PAGES = []
D = dict(group="guides", checked="27 Nov 2026", iso="2026-11-27")


def add(**kw):
    PAGES.append({**D, **kw})


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table-scroll"><table><thead><tr>{h}</tr></thead><tbody>\n{r}\n</tbody></table></div>'


NOTE = "<p>We make Swipeo, so weigh our row accordingly. Other rows only repeat what App Store listings say (Slidebox checked 23 Nov 2026, the rest 27 Nov 2026); we did not test those apps.</p>"
SWIPEO_ROW = ["Swipeo", "iPhone and iPad", "Swipe or tap, undo, in-app trash with restore, duplicate groups (not AI), months and albums, storage statistics", "Free with a daily limit; Premium weekly or yearly"]
PIXTIDE_ROW = ["Pixtide Swipe", "iPhone (iPad not listed)", "Keep, delete or later; undo; review before confirming; browse by month, year or category", "Free; one-time Pro purchase, no subscription"]
ODOA_ROW = ["Odoa", "iPhone (iPad not listed)", "Swipe, undo, review pile, duplicates, months, albums", "Free with in-app purchases"]
CLEVER_ROW = ["Clever Cleaner", "iPhone (iPad in compatibility mode)", "Swipe mode, AI grouping of duplicate and similar photos, large videos, screenshots", "Free with daily limits; weekly or lifetime purchase"]
SWIPEWIPE_ROW = ["Swipewipe", "Check the listing", "Swipe right to keep, left to delete; On This Day; month by month", "Free with in-app purchases"]
SLIDEBOX_ROW = ["Slidebox", "Check the listing", "Swipe to delete, undo, album sorting, compare similar photos", "Free with subscription or one-time purchase"]
HEAD = ["App", "Devices", "What the listing says", "Price model"]

SHOTS = '<h2>Screenshots</h2><div class="shots">' + "".join(
    f'<img src="../../assets/swipeo-{n}.jpg" width="600" height="1303" loading="lazy" alt="{a}">'
    for n, a in [
        ("swipe", "Swipeo swipe screen with keep, delete and undo buttons"),
        ("duplicates", "Swipeo duplicate group with a marked best photo and the others selected"),
        ("home", "Swipeo home screen with duplicates, screenshots, large videos, recents and on this day"),
        ("freed", "Swipeo summary screen showing space freed after a cleanup"),
    ]
) + '</div><p class="meta">App Store screenshots with sample data. The amount of space you free depends on your library.</p>'

add(
    slug="swipeo-photo-cleaner-app",
    title="What Is Swipeo? Swipe Photo Cleaner for iPhone and iPad",
    description="Swipeo is an iPhone and iPad app: swipe to keep or delete photos and videos, undo, restore from an in-app trash, review duplicates and see storage statistics.",
    h1="What is Swipeo?",
    lead="A photo and video cleaner for iPhone and iPad: you decide with a swipe, and deleted items wait in a trash first.",
    answer="<strong>Swipeo: Swipe to Delete Photos</strong> is an app for <strong>iPhone and iPad</strong>. You <strong>swipe or tap to keep or delete</strong>, can <strong>undo</strong>, and <strong>restore from the in-app trash</strong> before anything moves to Recently Deleted. It also shows <strong>duplicate groups</strong> and <strong>storage statistics</strong>. Photos are <strong>processed on the device</strong> and are not uploaded to Swipeo's servers.",
    body="<h2>Features</h2>" + table(["Feature", "What you get"], [
        ["Swipe review", "Photos and videos one card at a time; swipe or tap; undo"],
        ["In-app trash", "Restore, delete one or delete all; emptying it moves items to Recently Deleted in Photos"],
        ["Review sets", "Screenshots, recent, selfies, bursts, Live Photos, large videos, random, on this day"],
        ["Months and albums", "Clean one month or one album at a time"],
        ["Duplicates", "Groups with a Best badge; sort by newest, oldest or largest; not AI"],
        ["Statistics", "Storage overview, media types, monthly cleanup progress"],
        ["Devices", "iPhone and iPad, iOS / iPadOS 18.4 or later"],
        ["Languages", "English, Russian, Spanish, French, German, Italian, Chinese, Japanese, Korean"],
    ]) + """<h2>Privacy</h2>
<p>Swipeo works with the system Photos library on your device and does not upload your photos to its own servers. The app uses analytics and subscription services. If an original is stored only in iCloud, iOS may download it so it can be shown. See the App Privacy section of the App Store listing and the <a href="https://emilsvetlichnyy.github.io/swipeclean-privacy/">privacy policy</a>.</p>
<h2>Price</h2>
<p>Free to download. The free version has a daily limit on deletions, including one duplicate group a day. Premium, weekly or yearly, removes the limit. Current prices are on the App Store listing.</p>
<h2>What it does not do</h2>
<p>No AI detection of blurry or similar photos, no cloud storage and no sync of its own. With iCloud Photos on, deleting a photo also deletes it from iCloud.</p>""",
    after=SHOTS,
    faqs=[
        ("Does Swipeo work on iPad?", "Yes. It runs on iPhone and iPad with iOS or iPadOS 18.4 or later."),
        ("Does Swipeo upload my photos?", "It does not upload your photos to its own servers. Cleanup runs on the device. The app uses analytics and subscription services."),
        ("Can I undo a swipe?", "Yes. Use undo during a session, or restore the item from Swipeo's trash before you empty it."),
        ("Is Swipeo free?", "It is free to download with a daily limit on deletions. Premium removes the limit."),
        ("Does Swipeo use AI to find duplicates?", "No. It groups duplicates by type, resolution and capture time."),
    ],
    sources=[APPSTORE_SWIPEO_US, APPLE_DELETE],
    related=["photo-cleaner-no-cloud-upload", "tinder-style-photo-cleaner-iphone", "swipewipe-alternatives", "slidebox-alternatives"],
    swipeo=SW_SWIPE,
)

add(
    slug="swipewipe-alternatives",
    title="Swipewipe Alternatives for iPhone (2026)",
    description="Alternatives to Swipewipe compared: Swipeo, Slidebox, Pixtide Swipe and Odoa. Devices, undo and trash, duplicates and price model, with sources.",
    h1="Swipewipe alternatives for iPhone",
    lead="Pick by what you miss: iPad support, albums, a one-time purchase or a swipe review with a trash.",
    answer="Four options: <strong>Swipeo</strong> for iPhone and iPad with undo, an in-app trash and storage statistics; <strong>Slidebox</strong> if you also sort into albums; <strong>Pixtide Swipe</strong> if you want a one-time purchase instead of a subscription; <strong>Odoa</strong> for month-by-month progress with albums.",
    body=table(HEAD, [SWIPEWIPE_ROW, SWIPEO_ROW, SLIDEBOX_ROW, PIXTIDE_ROW, ODOA_ROW]) + NOTE,
    faqs=[
        ("Which Swipewipe alternative works on iPad?", "Swipeo lists iPhone and iPad. Pixtide Swipe and Odoa list iPhone but not iPad. Check the Slidebox listing for its devices."),
        ("Is there an alternative without a subscription?", "Pixtide Swipe lists a one-time Pro purchase and no subscription. Slidebox lists a one-time purchase option."),
    ],
    sources=[APPSTORE_SWIPEWIPE_US, APPSTORE_SWIPEO_US, APPSTORE_SLIDEBOX, APPSTORE_PIXTIDE, APPSTORE_ODOA],
    related=["best-swipe-photo-cleaner-apps-iphone", "slidebox-alternatives", "swipeo-photo-cleaner-app"],
    swipeo=SW_SWIPE,
)

add(
    slug="slidebox-alternatives",
    title="Slidebox Alternatives for iPhone (2026)",
    description="Alternatives to Slidebox compared: Swipeo, Swipewipe, Pixtide Swipe and Odoa. Devices, undo and trash, albums and price model, with sources.",
    h1="Slidebox alternatives for iPhone",
    lead="Slidebox centers on swiping and album sorting. Other apps put the weight elsewhere.",
    answer="Four options: <strong>Swipeo</strong> if you want a trash with restore before Recently Deleted, duplicate groups and storage statistics on iPhone or iPad; <strong>Odoa</strong> if albums matter; <strong>Swipewipe</strong> for month-by-month and On This Day review; <strong>Pixtide Swipe</strong> for a one-time purchase.",
    body=table(HEAD, [SLIDEBOX_ROW, SWIPEO_ROW, ODOA_ROW, SWIPEWIPE_ROW, PIXTIDE_ROW]) + NOTE,
    faqs=[
        ("Which alternative also sorts into albums?", "Odoa lists dropping photos into albums while you swipe. Swipeo lets you clean one album at a time but is not an album organizer."),
        ("Which alternative has a trash with restore?", "Swipeo has an in-app trash with restore. Odoa and Pixtide Swipe list a review step before photos are deleted."),
    ],
    sources=[APPSTORE_SLIDEBOX, APPSTORE_SWIPEO_US, APPSTORE_ODOA, APPSTORE_SWIPEWIPE_US, APPSTORE_PIXTIDE],
    related=["swipeo-vs-slidebox", "swipewipe-alternatives", "swipeo-photo-cleaner-app"],
    swipeo=SW_SWIPE,
)

add(
    slug="photo-cleaner-no-cloud-upload",
    title="Photo Cleaner Apps That Don't Upload Your Photos (iPhone)",
    description="Cleaner apps whose listings say photos stay on the device: Swipeo, Odoa, Pixtide Swipe and Clever Cleaner, with each App Privacy label and how to check it.",
    h1="Photo cleaner apps that don't upload your photos",
    lead="Look for two things: a statement that photos stay on the device, and an App Privacy label you are comfortable with.",
    answer="<strong>Swipeo</strong>, <strong>Odoa</strong>, <strong>Pixtide Swipe</strong> and <strong>Clever Cleaner</strong> each say in their App Store listing that photos are processed on the device or not uploaded. Their <strong>App Privacy labels differ</strong>: not uploading photos does not mean collecting no data.",
    body=table(["App", "What the listing says about photos", "App Privacy label (summary)"], [
        ["Swipeo", "Cleanup runs on device; no cloud upload", "Data not linked to you: identifiers, usage data, diagnostics"],
        ["Odoa", "Works on your iPhone; photos are never uploaded to their servers", "Data not linked to you: purchases, usage data, identifiers, diagnostics"],
        ["Pixtide Swipe", "Your photo library never leaves your phone", "Includes data linked to you, among it purchases, identifiers and usage data"],
        ["Clever Cleaner", "Everything is processed locally; photos and videos stay on your device", "Includes identifiers used to track you"],
    ]) + """<h2>How to check yourself</h2>
<ul><li>Read <strong>App Privacy</strong> on the listing.</li><li>Give <strong>Limited Photos access</strong> first if you are unsure.</li><li>Remember that iCloud Photos is Apple's own upload: it works regardless of the cleaner you use.</li></ul>
<p>These are developer statements and labels as of 27 Nov 2026, not an independent audit. We make Swipeo and did not test the other apps.</p>""",
    faqs=[
        ("Does Swipeo upload photos to a server?", "Swipeo does not upload your photos to its own servers. It uses analytics and subscription services."),
        ("Is the App Privacy label verified by Apple?", "Apple states that the label is provided by the developer. Treat it as the developer's declaration."),
    ],
    sources=[APPSTORE_SWIPEO_US, APPSTORE_ODOA, APPSTORE_PIXTIDE, APPSTORE_CLEVER],
    related=["are-photo-cleaner-apps-safe", "swipeo-photo-cleaner-app", "best-apps-to-free-up-iphone-storage-photos"],
    swipeo="Swipeo cleans the library on your device and holds deleted items in its own trash first.",
)

add(
    slug="tinder-style-photo-cleaner-iphone",
    title="Tinder-Style Photo Cleaner Apps: Swipe to Delete Photos",
    description="Apps that work like Tinder for your camera roll: swipe left to delete, right to keep. Swipeo, Swipewipe, Slidebox, Pixtide Swipe and Odoa compared.",
    h1="Tinder-style photo cleaner apps for iPhone",
    lead="One photo on screen, one decision: swipe to keep it or delete it.",
    answer="Apps that let you clean the camera roll Tinder-style include <strong>Swipeo</strong> (iPhone and iPad, undo, in-app trash), <strong>Swipewipe</strong> (month by month), <strong>Pixtide Swipe</strong> (swipe right to keep, left to delete, down for later) and <strong>Odoa</strong> (left to delete, right to keep). <strong>Slidebox</strong> also deletes by swiping and adds album sorting. These apps are not related to Tinder.",
    body=table(HEAD, [SWIPEO_ROW, SWIPEWIPE_ROW, PIXTIDE_ROW, ODOA_ROW, SLIDEBOX_ROW]) + NOTE,
    faqs=[
        ("Does the iPhone Photos app have swipe to delete?", "No. In Photos you select items and tap the trash icon. Swipe cleaners add the gesture."),
        ("What if I swipe the wrong way?", "Pick an app with undo or a trash. Swipeo has both, and iOS also keeps deleted photos in Recently Deleted for 30 days."),
    ],
    sources=[APPSTORE_SWIPEO_US, APPSTORE_SWIPEWIPE_US, APPSTORE_PIXTIDE, APPSTORE_ODOA, APPSTORE_SLIDEBOX, APPLE_DELETE],
    related=["swipe-to-delete-photos-iphone", "best-swipe-photo-cleaner-apps-iphone", "swipeo-photo-cleaner-app"],
    swipeo=SW_SWIPE,
)
