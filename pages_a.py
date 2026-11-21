from _src import *

PAGES = []


def add(**kw):
    kw.setdefault("group", "delete")
    PAGES.append(kw)


add(
    slug="delete-multiple-photos-iphone",
    title="How to Delete Multiple Photos on iPhone at Once",
    description="Delete many photos on iPhone in one go: tap Select, drag across thumbnails, tap Trash. Includes the Recently Deleted step that actually frees space.",
    h1="How to delete multiple photos on iPhone at once",
    lead="Select many photos in one gesture, then empty Recently Deleted to get the space back.",
    answer="Open <strong>Photos</strong>, tap <strong>Select</strong>, tap photos or <strong>drag your finger across</strong> several, then tap the <strong>Trash</strong> button and confirm. Deleted items stay in Recently Deleted for 30 days, so empty that album if you want the storage back right away.",
    steps=[
        "Open the Photos app and go to Library or an album.",
        "Tap <strong>Select</strong> in the top right.",
        "Tap photos one by one, or slide your finger across a row of thumbnails to select many. Swipe sideways first: swiping vertically scrolls the grid.",
        "Tap the <strong>Trash</strong> button, then confirm <strong>Delete</strong>.",
        "To free space now: Albums → Utilities → Recently Deleted → Select → Delete All.",
    ],
    body="""<h2>What to know</h2>
<table><thead><tr><th>Situation</th><th>What happens</th></tr></thead><tbody>
<tr><td>Normal delete</td><td>Photos move to Recently Deleted for 30 days</td></tr>
<tr><td>iCloud Photos is on</td><td>The delete applies to your other devices too</td></tr>
<tr><td>Trash button is grey</td><td>Photos were probably synced from a computer, see <a href="../../storage/cant-delete-photos-synced-from-computer/">this fix</a></td></tr>
</tbody></table>""",
    faqs=[
        ("Is there a limit to how many photos I can select?", "Apple does not state a hard limit on its Delete photos page. Very large selections can be slow, so work in batches if the phone lags."),
        ("Do deleted photos free storage immediately?", "No. They stay in Recently Deleted for 30 days unless you delete them there too."),
        ("Can I undo a bulk delete?", "Yes, within the 30 days: open Recently Deleted, select the items and tap Recover."),
    ],
    sources=[APPLE_DELETE, MACPAW_MULTI, POPSCI_SELECT],
    related=["select-all-photos-iphone", "empty-recently-deleted-iphone", "swipe-to-delete-photos-iphone"],
    swipeo="If selecting in a grid feels risky, go through photos one at a time instead: " + SW_SWIPE,
)

add(
    slug="select-all-photos-iphone",
    title="How to Select All Photos on iPhone (What Works)",
    description="Photos has no single Select All for the whole library. Here is where Select All does work (albums, days) and the faster workarounds.",
    h1="How to select all photos on iPhone",
    lead="There is no one-tap Select All for the entire library, but albums and drag-select get close.",
    answer="Apple's Photos app does not describe a whole-library Select All. In <strong>albums</strong>, tap <strong>Select</strong> and a <strong>Select All</strong> option appears at the top left (guides report it is missing in Recents and Imports). In the main grid, tap Select and drag your finger across thumbnails.",
    steps=[
        "Open Photos → Albums and choose an album such as Screenshots or Videos.",
        "Tap <strong>Select</strong>, then <strong>Select All</strong> (top left).",
        "In the main Library grid: tap <strong>Select</strong> and drag a finger down across thumbnails to extend the selection.",
        "Tap Trash to delete, or Share to move them.",
    ],
    body="""<h2>Where it works</h2>
<table><thead><tr><th>Place</th><th>Select All?</th></tr></thead><tbody>
<tr><td>Albums (Screenshots, Videos, Live Photos…)</td><td>Yes, via Select → Select All</td></tr>
<tr><td>Library → Days view</td><td>Per day or week</td></tr>
<tr><td>Recents / whole library</td><td>No single button; drag-select instead</td></tr>
</tbody></table>
<p>Source guides disagree slightly on which views offer it, and it can change with iOS updates. If you do not see the button, check on your own iOS version.</p>""",
    faqs=[
        ("Why is there no Select All in my Library?", "Apple's support pages do not describe one for the whole library. Albums and drag-select are the practical options."),
        ("Is selecting everything safe?", "Only if you have a backup. Deleting with iCloud Photos on also removes photos from your other devices."),
    ],
    sources=[POPSCI_SELECT, APPLE_DELETE, ("Gadget Hacks: Select all photos on iPhone", "https://ios.gadgethacks.com/how-to/use-trick-quickly-select-all-photos-videos-your-iphone-bulk-delete-share-0312925/")],
    related=["delete-multiple-photos-iphone", "delete-all-photos-iphone"],
    swipeo="Instead of selecting everything blindly, sort through photos and keep the ones you want. " + SW_SWIPE,
)

add(
    slug="delete-all-photos-iphone",
    title="How to Delete All Photos from iPhone Safely",
    description="Deleting every photo from an iPhone: what to back up first, how iCloud Photos changes the result, and how to empty Recently Deleted.",
    h1="How to delete all photos from iPhone",
    lead="Back up first, check iCloud Photos, then delete and empty Recently Deleted.",
    answer="Select your photos in Photos, tap Trash, then empty <strong>Recently Deleted</strong>. If <strong>iCloud Photos</strong> is on, the photos are deleted from iCloud and your other devices too, so back up anything you need before you start.",
    steps=[
        "Back up what you want to keep (computer, external drive or another service).",
        "Check Settings → [your name] → iCloud → Photos. If it is on, deleting here deletes everywhere.",
        "In Photos, select the photos (use albums with Select All, or drag-select) and tap Trash.",
        "Open Albums → Utilities → Recently Deleted, unlock it, tap Select → Delete All.",
    ],
    body="<p>If you only want to free storage and keep your photos, read <a href=\"../../storage/optimize-iphone-storage-vs-download-originals/\">Optimize iPhone Storage</a> first: deleting is the one action you cannot take back after 30 days.</p>",
    faqs=[
        ("Will deleting all photos from iPhone delete them from iCloud?", "If iCloud Photos is on, yes: the deletion syncs to iCloud and your other devices."),
        ("Can I recover them afterwards?", "For 30 days via Recently Deleted. After that they are gone unless you have a separate backup."),
    ],
    sources=[APPLE_DELETE, PETAPIXEL_ALL, APPLE_RECOVER],
    related=["does-deleting-iphone-photo-delete-icloud", "empty-recently-deleted-iphone", "delete-photos-keep-in-icloud"],
    swipeo="If you do not really want everything gone, review and keep the good ones, delete the rest. " + SW_SWIPE,
)

add(
    slug="delete-all-screenshots-iphone",
    title="How to Delete All Screenshots on iPhone at Once",
    description="Delete every screenshot on iPhone from the Screenshots album in a few taps, then empty Recently Deleted to free the space.",
    h1="How to delete all screenshots on iPhone at once",
    lead="Screenshots have their own album, so bulk deletion takes under a minute.",
    answer="In Photos go to <strong>Albums → Media Types → Screenshots</strong>, tap <strong>Select → Select All</strong>, tap the Trash icon and confirm. Then empty <strong>Recently Deleted</strong>, because the storage is not returned until the screenshots leave that album.",
    steps=[
        "Open Photos → Albums and scroll to <strong>Media Types</strong>.",
        "Tap <strong>Screenshots</strong>, then <strong>Select</strong> in the top right.",
        "Tap <strong>Select All</strong> (or pick specific screenshots) and tap the <strong>Trash</strong> icon.",
        "Confirm <strong>Delete</strong>, then empty Albums → Utilities → Recently Deleted.",
    ],
    body="""<h2>Keep a few?</h2>
<p>Before Select All, scroll once and tap the heart on the screenshots you want to keep (receipts, tickets, maps). Favorites are easy to filter later. Another route is a Shortcut that deletes old screenshots only: see <a href="../delete-old-screenshots-shortcut-iphone/">this guide</a>.</p>""",
    faqs=[
        ("Where are screenshots stored on iPhone?", "In the Photos app under Albums → Media Types → Screenshots."),
        ("Why did my storage not change?", "Deleted screenshots sit in Recently Deleted for 30 days. Delete them there to free space."),
    ],
    sources=[HOWTOGEEK_SHOTS, GADGET_SHOTS, APPLE_DELETE],
    related=["delete-old-screenshots-shortcut-iphone", "empty-recently-deleted-iphone", "iphone-photo-cleanup-checklist"],
    swipeo="Screenshots are usually the fastest clean-up: swipe through them, keep the few that matter, delete the rest. " + SW_SWIPE,
)

add(
    slug="delete-old-screenshots-shortcut-iphone",
    title="Delete Old Screenshots on iPhone with a Shortcut",
    description="Use the Shortcuts app to delete screenshots older than a date while keeping recent ones, favorites and hidden photos.",
    h1="Delete old screenshots on iPhone with a Shortcut",
    lead="A Shortcut can remove screenshots by age instead of deleting all of them.",
    answer="In the <strong>Shortcuts</strong> app, build a shortcut that finds Photos where the media type is Screenshot and the date is older than your cut-off, then runs <strong>Delete Photos</strong>. Published versions also exclude recent screenshots, hidden photos and favorites.",
    steps=[
        "Open Shortcuts → <strong>+</strong> to create a new shortcut.",
        "Add the action <strong>Find Photos</strong>. Filter: Media Type is Screenshot, Date Taken is before your cut-off date.",
        "Optionally add filters to exclude Favorites.",
        "Add <strong>Delete Photos</strong>, run the shortcut and confirm.",
        "Empty Recently Deleted to free the space.",
    ],
    body="<p>Action names can change between iOS versions. Test on a small date range first. The shortcut moves items to Recently Deleted, it does not bypass the 30-day window.</p>",
    faqs=[
        ("Is a Shortcut better than Select All?", "It is better if you want to keep recent screenshots. For a one-time wipe, the album's Select All is simpler."),
        ("Does it ask before deleting?", "iOS shows a confirmation for Delete Photos. Read the count before you confirm."),
    ],
    sources=[MENTALFLOSS_SHORTCUT, GADGET_SHOTS, APPLE_DELETE],
    related=["delete-all-screenshots-iphone", "empty-recently-deleted-iphone"],
    swipeo="Prefer to decide per screenshot rather than by date? " + SW_SWIPE,
)

add(
    slug="delete-duplicate-photos-iphone",
    title="How to Delete Duplicate Photos on iPhone",
    description="Use the built-in Duplicates album (iOS 16 and later) to merge exact copies, and what to do about near-duplicates it misses.",
    h1="How to delete duplicate photos on iPhone",
    lead="The Duplicates album handles exact copies; similar shots need a manual pass or an app.",
    answer="Open <strong>Photos → Albums → Utilities → Duplicates</strong>, tap <strong>Select</strong>, choose the items and tap <strong>Merge</strong>. The built-in tool only finds exact or near-exact copies. Near-identical shots taken a second apart are usually not counted as duplicates.",
    steps=[
        "Open Photos → Albums and scroll to <strong>Utilities</strong>.",
        "Tap <strong>Duplicates</strong> (iOS 16 and later).",
        "Tap <strong>Merge</strong> next to a set, or <strong>Select → Merge</strong> for several.",
        "Open Recently Deleted and delete the discarded copies to free space.",
    ],
    body="""<h2>What Merge does</h2>
<p>Merge keeps one version and moves the other copies to Recently Deleted. It does not free space until they are deleted from that album.</p>
<h2>What it misses</h2>
<p>Burst-like sequences, edited copies and slightly different angles are not exact duplicates. See <a href="../delete-similar-photos-iphone/">similar photos</a> and <a href="../delete-burst-photos-iphone/">burst photos</a>.</p>""",
    faqs=[
        ("Do I need an app to remove duplicates?", "No for exact copies: the Duplicates album is built in. An app helps with near-duplicates."),
        ("Why is the Duplicates album empty?", "Either there are no exact copies, or the library is still being analysed. It also needs iOS 16 or later."),
    ],
    sources=[PETAPIXEL_DUP, APPLE_STORAGE, MACPAW_SIMILAR],
    related=["merge-duplicate-photos-iphone", "delete-similar-photos-iphone", "empty-recently-deleted-iphone"],
    swipeo=f"Swipeo shows duplicates as groups (by type, resolution and capture time, not by AI) so you can pick what to keep. Deleting duplicates is part of Premium.",
)

add(
    slug="merge-duplicate-photos-iphone",
    title="What Does Merge Duplicates Do on iPhone Photos?",
    description="Merge in the Duplicates album keeps the best version and moves the other copies to Recently Deleted. Is it safe, and why storage may not drop.",
    h1="What does \"Merge Duplicates\" do on iPhone?",
    lead="It keeps one copy and sends the others to Recently Deleted.",
    answer="<strong>Merge</strong> in Photos → Utilities → Duplicates keeps one version of each set and moves the other copies to <strong>Recently Deleted</strong>. Storage only comes back after those copies are deleted there or after 30 days.",
    steps=[
        "Photos → Albums → Utilities → <strong>Duplicates</strong>.",
        "Review a set; tap <strong>Merge</strong> (or Select several sets → Merge).",
        "Confirm the number of copies to be merged.",
        "Then Recently Deleted → Select → Delete All, if you want the space now.",
    ],
    body="<p>Because the discarded copies sit in Recently Deleted, you can still recover one within 30 days if Merge picked the wrong version.</p>",
    faqs=[
        ("Is Merge safe?", "It is reversible for 30 days through Recently Deleted. Check a few sets before merging everything."),
        ("Does Merge combine edits or metadata?", "Apple describes it as keeping the best quality version; details of what is combined can vary by iOS version, so check Apple's current notes."),
    ],
    sources=[PETAPIXEL_DUP, APPLE_STORAGE, APPLE_DELETE],
    related=["delete-duplicate-photos-iphone", "empty-recently-deleted-iphone"],
    swipeo="Prefer to choose the keeper yourself? Swipeo shows duplicate groups and lets you decide which copy stays. Deleting duplicates is part of Premium.",
)

add(
    slug="delete-similar-photos-iphone",
    title="How to Find and Delete Similar Photos on iPhone",
    description="Near-identical photos are not caught by Apple's Duplicates tool. How to find similar shots by hand, with Favorites, or with an app.",
    h1="How to find and delete similar photos on iPhone",
    lead="Apple's Duplicates album only catches exact copies, so similar shots take a different approach.",
    answer="Photos finds <strong>exact duplicates</strong> only. For similar shots, scroll the Library in <strong>Days</strong> view and compare, mark your best shots with a <strong>heart</strong>, delete the rest, or use an app that groups similar photos taken at the same time.",
    steps=[
        "Open Photos → Library → <strong>Days</strong> to see shots grouped by day.",
        "Tap Select and tap the best photo of each near-identical group with a heart (Favorite).",
        "Delete the non-favorites from each group.",
        "Empty Recently Deleted to free the space.",
    ],
    body="<p>The Map view can also help: similar photos tend to share one location stamp. Do the pass in short sessions so you do not rush.</p>",
    faqs=[
        ("Is there an Apple tool for similar photos?", "Not for near-identical shots. Apple's Duplicates covers exact copies."),
        ("Are cleaner apps reliable at this?", "Results vary by app. Check the App Store privacy label and review what the app suggests before deleting."),
    ],
    sources=[MACPAW_SIMILAR, PETAPIXEL_DUP, ("Apple Community: Delete duplicate and similar photos", "https://discussions.apple.com/thread/256008771")],
    related=["delete-duplicate-photos-iphone", "delete-burst-photos-iphone", "swipe-to-delete-photos-iphone"],
    swipeo="Swipeo shows duplicate groups (by type, resolution and capture time) and lets you go through photos one by one. It does not claim AI detection: you decide what stays. " + SW_SWIPE,
)

add(
    slug="delete-blurry-photos-iphone",
    title="How to Find and Delete Blurry Photos on iPhone",
    description="iPhone Photos has no blur filter. Manual ways to spot blurry shots, and what third-party cleaners offer and ask for.",
    h1="How to find and delete blurry photos on iPhone",
    lead="There is no built-in blur finder, so it is a scroll, a swipe app or a third-party scan.",
    answer="iPhone <strong>Photos does not have a blur filter</strong>. You can scroll the grid at a larger thumbnail size and delete blurry shots by hand, or use an app. Some cleaners scan for blur, so check each app's privacy label before giving it full photo access.",
    steps=[
        "Open Photos → Library and pinch to make thumbnails larger.",
        "Tap <strong>Select</strong> and tap each blurry photo.",
        "Tap Trash, then empty Recently Deleted.",
        "If a shot is only slightly soft, try the Edit tools (sharpness) instead of deleting it.",
    ],
    body="""<h2>Options compared</h2>
<table><thead><tr><th>Option</th><th>Finds blur automatically?</th></tr></thead><tbody>
<tr><td>Apple Photos</td><td>No</td></tr>
<tr><td>Google Photos (if backed up there)</td><td>Reported to flag blurry shots under Manage storage</td></tr>
<tr><td>Third-party cleaners</td><td>Some do; privacy and pricing vary</td></tr>
<tr><td>Manual review</td><td>No, but you stay in control</td></tr>
</tbody></table>""",
    faqs=[
        ("Can iPhone find blurry photos?", "Not with a built-in tool. Photos offers no blur filter."),
        ("Is it safe to let a cleaner scan my photos?", "Check the privacy label and whether processing is on-device. See the safety guide on this site."),
    ],
    sources=[LAPTOP_BLUR, MACPAW_SIMILAR, ("Apple Community: Blurry images in Photos", "https://discussions.apple.com/thread/256027737")],
    related=["are-photo-cleaner-apps-safe", "swipe-to-delete-photos-iphone", "delete-similar-photos-iphone"],
    swipeo="Swipeo does not claim to detect blur automatically. It makes the manual pass quick: one photo at a time, swipe to keep or delete, review the trash. " + "",
)

add(
    slug="delete-live-photos-keep-still-iphone",
    title="Delete Live Photos but Keep the Still Photo on iPhone",
    description="Convert Live Photos to stills with Duplicate as Still Photo, then delete the originals and empty Recently Deleted to reclaim space.",
    h1="How to delete Live Photos but keep the still photo",
    lead="Make a still copy first, then delete the Live original. Duplicating alone frees nothing.",
    answer="Go to <strong>Albums → Media Types → Live Photos</strong>, tap Select, choose the photos, tap the <strong>⋯ menu → Duplicate → Duplicate as Still Photo</strong>, then <strong>delete the original Live Photos</strong> and empty Recently Deleted. Check your own storage afterwards: one user reported the still was the same size as the original.",
    steps=[
        "Photos → Albums → <strong>Live Photos</strong>.",
        "Tap Select and pick the Live Photos you want to convert.",
        "Tap <strong>⋯ → Duplicate → Duplicate as Still Photo</strong>.",
        "Delete the original Live Photos (they stay until you do).",
        "Empty Albums → Utilities → Recently Deleted.",
    ],
    body="<p>Test on a few photos first and compare Settings → General → iPhone Storage before and after, because the saving depends on the photo.</p>",
    faqs=[
        ("Does duplicating as still free space?", "Not by itself: the original Live Photo remains until you delete it."),
        ("Do I lose the video part?", "In the still copy, yes. The motion is not kept."),
    ],
    sources=[CLEVER_LIVE, ("Apple Community: Convert Live Photos to regular photos", "https://discussions.apple.com/thread/256217692"), APPLE_DELETE],
    related=["empty-recently-deleted-iphone", "iphone-storage-full-photos"],
    swipeo="Swipeo has a Live Photos set to go through one by one. It does not convert Live Photos to stills.",
)

add(
    slug="delete-burst-photos-iphone",
    title="How to Delete Burst Photos on iPhone and Keep the Best",
    description="Keep only your favorite frames from a burst and delete the rest. Includes tips to stop accidental bursts.",
    h1="How to delete burst photos on iPhone",
    lead="Pick the keepers inside a burst, then remove the rest.",
    answer="Open the burst in Photos, tap <strong>Select</strong>, tap the frames you want to keep, tap <strong>Done</strong> and choose <strong>Keep Only Favorites</strong>. The other frames are removed to Recently Deleted. Empty that album to free the space.",
    steps=[
        "Open the burst (it looks like a stack of photos) and tap <strong>Select</strong>.",
        "Tap the frames you want. Gray dots below thumbnails are Apple's suggestions.",
        "Tap <strong>Done</strong>, then choose to keep only your favorite(s).",
        "Empty Recently Deleted to free storage.",
    ],
    body="<p>To avoid accidental bursts, turn on <strong>Use Volume Up for Burst</strong> in Settings → Camera or switch burst behaviour off.</p>",
    faqs=[
        ("Why do burst photos take so much space?", "A burst stores many frames from one moment. Keeping one or two usually frees most of it."),
        ("A burst will not delete. What now?", "One reported workaround is to quit and reopen Photos and try again. It is an anecdote, not an official fix."),
    ],
    sources=[APPLE_BURST, MACRUMORS_BURST, APPLE_DELETE],
    related=["delete-similar-photos-iphone", "empty-recently-deleted-iphone"],
    swipeo="For the rest of your library, go photo by photo. " + SW_SWIPE,
)
