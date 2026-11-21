from _src import *

PAGES = []


def add(**kw):
    kw.setdefault("group", "delete")
    PAGES.append(kw)


add(
    slug="delete-large-videos-iphone",
    title="How to Delete Large Videos on iPhone to Free Space",
    description="Videos are usually the biggest items in Photos. How to find the longest ones, delete them, and what to export first.",
    h1="How to delete large videos on iPhone",
    lead="Long videos take the most room. Find them, export what you want to keep, delete the rest.",
    answer="Open <strong>Photos → Albums → Videos</strong> and look for the longest clips: duration is the best clue to size, because Photos has no built-in sort by file size. Delete them, then empty <strong>Recently Deleted</strong> to get the space back. Export anything you want to keep first.",
    steps=[
        "Photos → Albums → <strong>Videos</strong> (also check Slo-mo and Screen Recordings).",
        "Scan for the longest durations. Tap the info (i) button on a video to check details.",
        "To keep a video, share or export the original to iCloud Drive, a computer or another storage first.",
        "Select the videos you do not need and tap Trash.",
        "Empty Albums → Utilities → Recently Deleted.",
    ],
    body="<p>Heavy formats add up: one source notes that 60 seconds of 4K footage can use close to half a gigabyte on the phone. Settings → Camera → Record Video lets you change the recording format for future clips.</p>",
    faqs=[
        ("Does Photos sort videos by size?", "Most guides say no. The Files app can sort by size for files, but not Photos items."),
        ("Why is my storage still full after deleting videos?", "They are still in Recently Deleted for 30 days, or iCloud sync has not finished."),
    ],
    sources=[CLEVER_SORT, MACRUMORS_GUIDE, APPLE_STORAGE],
    related=["find-large-videos-iphone", "delete-screen-recordings-iphone", "empty-recently-deleted-iphone"],
    swipeo="Swipeo has a Large videos set, so the heavy ones come first. " + SW_SWIPE,
)

add(
    slug="find-large-videos-iphone",
    title="How to Find Large Videos on iPhone (Sort by Size)",
    description="Photos cannot sort by size. Practical ways to find the biggest videos: duration, albums, iPhone Storage and size-sorting apps.",
    h1="How to find large videos on iPhone",
    lead="Photos has no size sort. These workarounds find the heavy clips.",
    answer="<strong>Photos cannot sort by file size.</strong> Check the <strong>Videos</strong> and <strong>Screen Recordings</strong> albums for long durations, look at <strong>Settings → General → iPhone Storage → Photos</strong>, or use a cleaner that lists videos by size.",
    steps=[
        "Open Photos → Albums → Videos and read the duration badges, longest first by eye.",
        "Do the same in Screen Recordings and Slo-mo.",
        "Settings → General → iPhone Storage: check the Photos entry and any storage recommendations.",
        "Optional: use a size-sorting app, and check what access it requests.",
    ],
    body="<p>Sources disagree on whether any built-in sort exists; most say no, and an old \"Review Personal Videos\" suggestion is reported as no longer available.</p>",
    faqs=[
        ("Can I sort Photos by size in the Files app?", "The Files app sorts files by size, but Photos library items are not normal files there."),
        ("Which videos are usually the biggest?", "Long 4K clips, slow-motion videos and screen recordings."),
    ],
    sources=[CLEVER_SORT, ("MacRumors forum: find huge videos", "https://forums.macrumors.com/threads/how-to-find-those-huge-videos-that-take-lots-of-space-on-the-iphone.2237541"), APPLE_STORAGE],
    related=["delete-large-videos-iphone", "delete-screen-recordings-iphone"],
    swipeo="Swipeo has a Large videos set, so heavy clips are not buried in the grid. " + SW_SWIPE,
)

add(
    slug="delete-screen-recordings-iphone",
    title="How to Delete Screen Recordings on iPhone",
    description="Screen recordings pile up and are often large. Find them in Media Types, delete in bulk, and empty Recently Deleted.",
    h1="How to delete screen recordings on iPhone",
    lead="They live in their own album, which makes them easy to clear in bulk.",
    answer="In Photos open <strong>Albums → Media Types → Screen Recordings</strong>, tap <strong>Select</strong>, pick the recordings (or Select All), tap <strong>Trash</strong>, then empty <strong>Recently Deleted</strong>.",
    steps=[
        "Photos → Albums → <strong>Media Types</strong> → <strong>Screen Recordings</strong>.",
        "Tap Select; scan durations and pick the ones to delete.",
        "Tap Trash and confirm.",
        "Albums → Utilities → Recently Deleted → Select → Delete All.",
    ],
    body="<p>Screen recordings are long and usually disposable, which is why guides point to this album first when you need space fast.</p>",
    faqs=[
        ("Do screen recordings count as videos?", "Yes. They are saved in Photos and also appear in Videos."),
        ("Can I delete just the old ones?", "Sort by date in the album and select the older block with drag-select."),
    ],
    sources=[CLEVER_SORT, HOWTOGEEK_SHOTS, APPLE_DELETE],
    related=["find-large-videos-iphone", "delete-large-videos-iphone", "delete-all-screenshots-iphone"],
    swipeo="Swipe through old recordings and keep only the ones you still need. " + SW_SWIPE,
)

add(
    slug="delete-hidden-photos-iphone",
    title="How to Delete Hidden Photos on iPhone",
    description="Hidden photos sit in a locked Hidden album. Unlock it with Face ID, Touch ID or passcode, then delete and empty Recently Deleted.",
    h1="How to delete hidden photos on iPhone",
    lead="The Hidden album is locked by default: unlock it, delete, and clear Recently Deleted.",
    answer="Open <strong>Albums → Utilities → Hidden</strong>, unlock it with Face ID, Touch ID or your passcode, tap <strong>Select</strong>, choose the photos and tap <strong>Trash</strong>. They then go to Recently Deleted for 30 days unless you delete them there as well.",
    steps=[
        "Photos → Albums → Utilities → <strong>Hidden</strong>.",
        "Authenticate (Face ID, Touch ID or passcode).",
        "Tap Select, pick the photos and tap Trash.",
        "Open Recently Deleted (also locked) and delete them for good if you want the space now.",
    ],
    body="<p>If you only want to hide the album itself, turn off <strong>Show Hidden Album</strong> in Photos settings. That does not delete any photo. With iCloud Photos on, hiding and deleting sync to your other devices.</p>",
    faqs=[
        ("Why does Photos ask for Face ID?", "Apple locks the Hidden and Recently Deleted albums by default."),
        ("Does hiding free storage?", "No. Hidden photos still use space until you delete them."),
    ],
    sources=[APPLE_HIDDEN, APPLE_DELETE, ("MacRumors: Lock Hidden and Recently Deleted albums", "https://www.macrumors.com/how-to/lock-hidden-recently-deleted-photo-albums-ios/")],
    related=["empty-recently-deleted-iphone", "iphone-storage-full-photos"],
    swipeo="Swipeo works with the photos in your main library. Hidden items are handled by iOS settings, so unhide them first if you want to review them.",
)

add(
    slug="delete-large-attachments-messages-iphone",
    title="Delete Large Attachments in Messages on iPhone",
    description="Messages photos and videos can use a lot of storage. Use iPhone Storage → Messages → Review Large Attachments to remove them and keep chats.",
    h1="How to delete large attachments in Messages on iPhone",
    lead="Remove the heavy media and keep the conversations.",
    answer="Go to <strong>Settings → General → iPhone Storage</strong>, open <strong>Messages</strong> (or the recommendation <strong>Review Large Attachments</strong>), review photos, videos and GIFs, and delete the ones you do not need. The text of your chats stays.",
    steps=[
        "Settings → General → <strong>iPhone Storage</strong>.",
        "Tap <strong>Messages</strong> (or the Review Large Attachments recommendation).",
        "Browse Top Conversations, Photos, Videos, GIFs & Stickers.",
        "Swipe left on an item or tap Edit, then delete.",
    ],
    body="<p>If Messages is synced with iCloud, deleting an attachment also removes the cloud copy. Free space can take a few minutes to update.</p>",
    faqs=[
        ("Will my conversations be deleted?", "No. This only removes the attachments, per the guides."),
        ("Why can I not delete an attachment?", "An Apple Community thread suggests restarting the iPhone first."),
    ],
    sources=[MACRUMORS_ATTACH, APPLE_STORAGE, ("Apple Community: Review Large Attachments", "https://discussions.apple.com/thread/252444280")],
    related=["iphone-storage-full-photos", "free-up-iphone-storage-without-deleting-photos"],
    swipeo="Swipeo cleans the photo library. Attachments inside Messages are separate, so use the steps above for those.",
)

add(
    slug="swipe-to-delete-photos-iphone",
    title="How to Swipe to Delete Photos on iPhone",
    description="Photos has no swipe-to-delete. Swipe-style cleaner apps show one photo at a time: swipe to keep or delete. What a safe one should include.",
    h1="How to swipe to delete photos on iPhone",
    lead="The Photos app has no swipe-to-delete. Swipe cleaners add it, and a good one includes a trash.",
    answer="Apple's Photos app deletes with <strong>Select → Trash</strong>; it has <strong>no swipe-to-delete</strong>. Swipe cleaner apps show one photo at a time: <strong>swipe one way to keep, the other to delete</strong>. Pick one with a <strong>trash or undo step</strong> before final deletion.",
    steps=[
        "Install a swipe cleaner and allow access to your Photos library.",
        "Swipe or tap to keep or delete each photo or video.",
        "Review the app's trash (a safe one holds deleted items before the final step).",
        "Confirm the final deletion in the iOS prompt, then empty Recently Deleted.",
    ],
    body="""<h2>What to look for</h2>
<table><thead><tr><th>Feature</th><th>Why it matters</th></tr></thead><tbody>
<tr><td>In-app trash or undo</td><td>Swiping fast makes mistakes; you want a way back</td></tr>
<tr><td>Processing on the device</td><td>Your photos should not be uploaded to clean them</td></tr>
<tr><td>Sort by month or type</td><td>Makes a big library manageable</td></tr>
<tr><td>Clear free limits</td><td>Many apps cap free deletions</td></tr>
</tbody></table>
<p>Compare real options in <a href="../../guides/best-swipe-photo-cleaner-apps-iphone/">swipe photo cleaner apps for iPhone</a>.</p>""",
    faqs=[
        ("Is swiping faster than Select?", "For deciding photo by photo, yes. For clearing a whole album, Select All is faster."),
        ("Can I undo a swipe?", "In a swipe app with a trash, yes. After final deletion, iOS keeps items in Recently Deleted for 30 days."),
    ],
    sources=[APPSTORE_CLEANCAMERA, APPSTORE_WYPRR, APPSTORE_SWIPER, APPLE_DELETE],
    related=["best-swipe-photo-cleaner-apps-iphone", "are-photo-cleaner-apps-safe", "organize-iphone-photos-by-month"],
    swipeo="This is what Swipeo does: swipe or tap to keep or delete, a trash you can review, and duplicate groups. Processing uses the system Photos library on the device.",
)

# ---------------------------------------------------------------- storage

add(
    group="storage",
    slug="iphone-storage-full-photos",
    title="iPhone Storage Full? Free Up Space Used by Photos",
    description="When photos fill your iPhone: check Photos storage, turn on Optimize iPhone Storage, delete the biggest items and empty Recently Deleted.",
    h1="iPhone storage full: free up space used by photos",
    lead="A quick order of operations that works before you delete memories.",
    answer="Check <strong>Settings → General → iPhone Storage</strong>, turn on <strong>Optimize iPhone Storage</strong> if you use iCloud Photos, delete the biggest items (long videos, screenshots, duplicates), then empty <strong>Recently Deleted</strong>. Deleting alone does not free space until that last step.",
    steps=[
        "Settings → General → iPhone Storage: see what is big and read the recommendations.",
        "Settings → [your name] → iCloud → Photos: choose <strong>Optimize iPhone Storage</strong> if you have enough iCloud space.",
        "Delete screenshots, duplicates and long videos.",
        "Empty Albums → Utilities → Recently Deleted.",
        "Check Messages attachments and offload unused apps.",
    ],
    body="""<table><thead><tr><th>Action</th><th>Frees space?</th></tr></thead><tbody>
<tr><td>Delete photos</td><td>Only after Recently Deleted is emptied</td></tr>
<tr><td>Optimize iPhone Storage</td><td>Yes: keeps smaller versions, originals in iCloud</td></tr>
<tr><td>Offload unused apps</td><td>Yes, keeps app data</td></tr>
<tr><td>Review large attachments</td><td>Yes</td></tr>
</tbody></table>""",
    faqs=[
        ("Why is my iPhone storage full with few photos?", "Videos, Messages attachments, apps and system data count too. Check the iPhone Storage breakdown."),
        ("Is iCloud a replacement for local space?", "Optimized photos still keep smaller local copies, so it reduces but does not remove local use."),
    ],
    sources=[APPLE_STORAGE, MACRUMORS_GUIDE, TOMS_NO_DELETE],
    related=["storage-not-freeing-after-deleting-photos", "optimize-iphone-storage-vs-download-originals", "delete-large-videos-iphone"],
    swipeo="Swipeo helps with the manual part: swipe through screenshots, videos and duplicates and delete what you do not need. " + SW_SWIPE,
)

add(
    group="storage",
    slug="photos-taking-so-much-storage-iphone",
    title="Why Is Photos Taking So Much Storage on My iPhone?",
    description="Common reasons the Photos entry is huge: videos, high-resolution shots, optimized iCloud previews and support files. What to check.",
    h1="Why is Photos taking so much storage on my iPhone?",
    lead="Usually videos and high-resolution originals, plus some overhead you cannot see.",
    answer="Most of the space is usually <strong>videos and high-resolution photos</strong>. Even with <strong>Optimize iPhone Storage</strong> on, the phone keeps smaller versions and the Photos total includes <strong>database and support files</strong>. Messages images may also be counted.",
    steps=[
        "Settings → General → iPhone Storage → Photos: note the size and the recommendations.",
        "Settings → [your name] → iCloud → Photos: confirm Optimize iPhone Storage is selected.",
        "Delete the largest videos and duplicates, then empty Recently Deleted.",
        "Check Messages attachments separately.",
    ],
    body="<p>Several Apple Community threads report a large Photos number with a modest library. Causes reported: previews kept by Optimize, support files, and sometimes a display glitch after an update. Treat the glitch reports as anecdotes.</p>",
    faqs=[
        ("Why is Photos bigger than my photo count suggests?", "Video and originals dominate. Database files add overhead."),
        ("Does Recently Deleted count?", "Yes, until the items are permanently deleted."),
    ],
    sources=[("Apple Community: Why is Photos taking so much storage?", "https://discussions.apple.com/thread/255990691"), APPLE_STORAGE, MACRUMORS_GUIDE],
    related=["iphone-storage-full-photos", "storage-not-freeing-after-deleting-photos", "delete-large-videos-iphone"],
    swipeo="Swipeo has a Large videos set and duplicate groups to review first. " + SW_SWIPE,
)

add(
    group="storage",
    slug="storage-not-freeing-after-deleting-photos",
    title="iPhone Storage Not Going Down After Deleting Photos",
    description="Why deleted photos do not free space: Recently Deleted, iCloud sync, restarts and big batches. A checklist of fixes.",
    h1="iPhone storage not going down after deleting photos",
    lead="Nine times in ten the photos are still in Recently Deleted.",
    answer="Deleted photos keep using space until they leave <strong>Recently Deleted</strong> (up to 30 days). Open <strong>Albums → Utilities → Recently Deleted → Select → Delete All</strong>, wait for it to finish and restart. If it still does not move, check iCloud Photos sync and delete in smaller batches.",
    steps=[
        "Albums → Utilities → <strong>Recently Deleted</strong> (unlock it).",
        "Tap Select → <strong>Delete All</strong>. If the album is very full, delete in small batches.",
        "Restart the iPhone and recheck Settings → General → iPhone Storage (it can lag a few minutes).",
        "Settings → [your name] → iCloud → Photos: check that sync has no errors, then delete again and choose Delete From All Devices.",
    ],
    body="""<table><thead><tr><th>Cause</th><th>Fix</th></tr></thead><tbody>
<tr><td>Items still in Recently Deleted</td><td>Delete All there</td></tr>
<tr><td>Album too full to empty</td><td>Delete in small batches</td></tr>
<tr><td>iCloud sync not finished</td><td>Wait, check sync status, retry</td></tr>
<tr><td>Storage figure not refreshed</td><td>Restart and wait</td></tr>
</tbody></table>""",
    faqs=[
        ("Why did deleted photos come back?", "iCloud sync can restore items in some cases. A few threads report photos reappearing in Recently Deleted without a confirmed fix."),
        ("How long until the space returns?", "Immediately after the items are deleted from Recently Deleted, though the display can lag."),
    ],
    sources=[CLEVER_STILL_FULL, ("Apple Community: Storage not freeing up", "https://discussions-jp-prz.apple.com/en/thread/255933635"), APPLE_DELETE],
    related=["empty-recently-deleted-iphone", "does-deleting-iphone-photo-delete-icloud", "iphone-storage-full-photos"],
    swipeo="Swipeo deletes through the system Photos library, so the same rule applies: empty Recently Deleted after cleaning to see the space come back.",
)

add(
    group="storage",
    slug="empty-recently-deleted-iphone",
    title="How to Empty Recently Deleted on iPhone (Free Space Now)",
    description="Permanently delete photos from the Recently Deleted album: Albums, Utilities, Recently Deleted, Select, Delete All.",
    h1="How to empty Recently Deleted on iPhone",
    lead="This is the step that actually returns the storage.",
    answer="Photos → <strong>Albums → Utilities → Recently Deleted</strong> → unlock with Face ID, Touch ID or passcode → <strong>Select → Delete All</strong>. After that the photos are permanently gone and the space is freed.",
    steps=[
        "Open Photos → Albums → scroll to Utilities.",
        "Tap <strong>Recently Deleted</strong> and unlock it.",
        "Tap <strong>Select</strong>, then <strong>Delete All</strong> (or choose specific items and tap Delete).",
        "Confirm. This cannot be undone.",
    ],
    body="<p>Anything left there is removed automatically after 30 days. If you are not sure about some photos, tap <strong>Recover</strong> on those first.</p>",
    faqs=[
        ("Can I get photos back after Delete All?", "Not from the phone. Only a separate backup may help."),
        ("Is it safe to delete everything in Recently Deleted?", "Yes if you have checked it. Scan the thumbnails once first."),
    ],
    sources=[APPLE_DELETE, APPLE_RECOVER, CLEVER_STILL_FULL],
    related=["how-long-recently-deleted-iphone", "recover-deleted-photos-iphone", "storage-not-freeing-after-deleting-photos"],
    swipeo="After you finish a cleaning session in Swipeo, empty Recently Deleted to get the space back.",
)
