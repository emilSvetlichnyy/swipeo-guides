from _src import *

PAGES = []


def add(**kw):
    kw.setdefault("group", "storage")
    PAGES.append(kw)


add(
    slug="how-long-recently-deleted-iphone",
    title="How Long Do Deleted Photos Stay on iPhone? (30 Days)",
    description="Deleted photos stay in Recently Deleted for 30 days, then are permanently removed. What that means for storage and recovery.",
    h1="How long do deleted photos stay on iPhone?",
    lead="30 days in Recently Deleted, unless you delete them there sooner.",
    answer="Apple says items in <strong>Recently Deleted</strong> stay for <strong>30 days</strong>, after which they are permanently deleted and cannot be recovered. You can remove them sooner with Select → Delete All, which also frees the storage.",
    body="""<table><thead><tr><th>Day</th><th>State</th></tr></thead><tbody>
<tr><td>0</td><td>You delete a photo. It moves to Recently Deleted and still uses space</td></tr>
<tr><td>1–29</td><td>You can Recover it or Delete it for good</td></tr>
<tr><td>30</td><td>It is removed automatically</td></tr>
</tbody></table>
<p>The exact per-photo countdown is not clearly documented; an Apple Community thread asks about it without a definitive answer, so do not rely on the last day.</p>""",
    faqs=[
        ("Can I change the 30 days?", "Not in the settings that Apple documents."),
        ("Does iCloud keep photos longer?", "A community answer says iCloud Photos does not keep them in Recently Deleted longer than the phone does. Treat that as unofficial."),
    ],
    sources=[APPLE_DELETE, APPLE_RECOVER, ("Apple Community: How 30 days from deletion is calculated", "https://discussions.apple.com/thread/256239791")],
    related=["recover-deleted-photos-iphone", "empty-recently-deleted-iphone"],
    swipeo="Swipeo adds its own short trash before the iPhone's Recently Deleted, so there are two chances to change your mind.",
)

add(
    slug="recover-deleted-photos-iphone",
    title="How to Recover Deleted Photos on iPhone",
    description="Recover photos from Recently Deleted within 30 days: Albums, Utilities, Recently Deleted, Select, Recover. What to do after 30 days.",
    h1="How to recover deleted photos on iPhone",
    lead="Within 30 days it is two taps. After that you need a backup.",
    answer="Open <strong>Photos → Albums → Utilities → Recently Deleted</strong>, unlock it, tap <strong>Select</strong>, choose the photos and tap <strong>Recover</strong>. After 30 days they are permanently deleted and only a separate backup can bring them back.",
    steps=[
        "Photos → Albums → Utilities → <strong>Recently Deleted</strong>.",
        "Unlock with Face ID, Touch ID or passcode.",
        "Tap Select, pick the photos and tap <strong>Recover</strong> at the bottom.",
        "The photos return to their original place in your library.",
    ],
    body="<p>If you used a cleaner app with its own trash, check that first. It may still hold the items before they reach Recently Deleted. Beyond 30 days, community answers suggest a device or iCloud backup, which is not official guidance.</p>",
    faqs=[
        ("Can I recover photos deleted from Recently Deleted?", "Not from the phone. Only an earlier backup may contain them."),
        ("Will recovered photos return to iCloud?", "With iCloud Photos on, recovered items sync again like normal library items."),
    ],
    sources=[APPLE_RECOVER, APPLE_DELETE, ("Apple Community: Recover photos deleted from Recently Deleted", "https://discussions.apple.com/thread/256237719")],
    related=["how-long-recently-deleted-iphone", "empty-recently-deleted-iphone"],
    swipeo="In Swipeo, items you delete wait in the app's trash and can be restored before you empty it.",
)

add(
    slug="cant-delete-photos-synced-from-computer",
    title="Can't Delete Photos on iPhone: Trash Icon Greyed Out",
    description="A greyed-out trash icon usually means photos were synced from a computer. Fix it from Finder or iTunes, or turn off iCloud Photos.",
    h1="Can't delete photos on iPhone: trash icon greyed out",
    lead="The photos came from a computer sync, so the phone is not allowed to delete them.",
    answer="A <strong>greyed-out Trash</strong> usually means the photos were <strong>synced from a computer</strong>. Delete them by changing the sync on that computer (Finder or iTunes: untick the photos or albums, then sync), or, if they came from a different computer, turn off iCloud Photos on the iPhone.",
    steps=[
        "Connect the iPhone to the computer you synced from.",
        "In Finder (Mac) or iTunes/Apple Devices (Windows), open the Photos tab.",
        "Untick the albums or folders you no longer want, then sync.",
        "If the photos came from another computer, try Settings → [your name] → iCloud → Photos → turn off, after making sure you have a copy.",
    ],
    body="<p>Back up first: if the phone holds the only copy, removing it deletes your only copy. Do not turn off iCloud Photos casually: if you delete before turning it off, items can be removed everywhere.</p>",
    faqs=[
        ("Why is the trash icon missing?", "Synced items are managed by the computer, not by the iPhone."),
        ("Is there a way without a computer?", "Reports mention turning off iCloud Photos, but it carries risk. Use a backup first."),
    ],
    sources=[MACWORLD_GREY, ("Apple Community: Trash can greyed out", "https://discussions.apple.com/thread/251776841"), APPLE_DELETE],
    related=["delete-multiple-photos-iphone", "does-deleting-iphone-photo-delete-icloud"],
    swipeo="Swipeo can only delete what iOS allows. Photos synced from a computer have to be removed with the steps above.",
)

add(
    slug="delete-photos-keep-in-icloud",
    title="Delete Photos from iPhone but Keep Them in iCloud",
    description="With iCloud Photos on, deleting removes the iCloud copy too. Use Optimize iPhone Storage to keep originals in iCloud and free space on the phone.",
    h1="How to delete photos from iPhone but keep them in iCloud",
    lead="You cannot, if iCloud Photos is on. Optimize Storage is the supported way.",
    answer="With <strong>iCloud Photos on</strong>, deleting a photo on iPhone <strong>deletes it from iCloud and your other devices</strong>. To free iPhone space and keep originals, choose <strong>Optimize iPhone Storage</strong>: the phone keeps smaller versions and iCloud keeps the full-resolution files.",
    steps=[
        "Settings → [your name] → iCloud → Photos.",
        "Make sure <strong>Sync this iPhone</strong> is on.",
        "Select <strong>Optimize iPhone Storage</strong>.",
        "Give it time to upload and replace originals with smaller copies.",
    ],
    body="<p>Forum answers add that Apple offers no cloud-only storage, and turning iCloud Photos off to delete can bring photos back when you turn it on again. If you want a separate copy, export to a computer first.</p>",
    faqs=[
        ("Is Optimize iPhone Storage the same as deleting?", "No. Nothing is lost: full-resolution files stay in iCloud."),
        ("What if my iCloud is full?", "Optimize depends on iCloud space. You may need a larger plan or a separate backup."),
    ],
    sources=[APPLE_STORAGE, MACWORLD_ICLOUD, ("Apple Community: Delete from iPhone but keep in iCloud", "https://discussions.apple.com/thread/253602469")],
    related=["does-deleting-iphone-photo-delete-icloud", "optimize-iphone-storage-vs-download-originals"],
    swipeo="Before you clean with any app, know that deleting here also deletes from iCloud Photos. Swipeo goes through the system library, so this applies to Swipeo as well.",
)

add(
    slug="does-deleting-iphone-photo-delete-icloud",
    title="Does Deleting a Photo on iPhone Delete It from iCloud?",
    description="Yes, if iCloud Photos is on: deleting on one device deletes on all. Recently Deleted keeps it 30 days before it is permanent.",
    h1="Does deleting a photo on iPhone delete it from iCloud?",
    lead="With iCloud Photos on, yes: the delete is synced everywhere.",
    answer="<strong>Yes, if iCloud Photos is on.</strong> A photo deleted on iPhone is removed from iCloud and your other devices signed in to the same account. It sits in Recently Deleted for 30 days first. If iCloud Photos is off, the delete only affects the phone.",
    body="""<table><thead><tr><th>iCloud Photos</th><th>Delete on iPhone</th></tr></thead><tbody>
<tr><td>On</td><td>Removed from iCloud and other devices (30 days in Recently Deleted)</td></tr>
<tr><td>Off</td><td>Removed only from this iPhone</td></tr>
</tbody></table>
<p>Apple's prompt may offer <strong>Delete From All Devices</strong> in some flows. Read it before confirming.</p>""",
    faqs=[
        ("Can I delete only from the iPhone?", "Not while iCloud Photos is syncing. Optimize iPhone Storage keeps the original in iCloud while freeing space on the phone."),
        ("How do I check if iCloud Photos is on?", "Settings → [your name] → iCloud → Photos."),
    ],
    sources=[APPLE_DELETE, APPLE_STORAGE, MACWORLD_ICLOUD],
    related=["delete-photos-keep-in-icloud", "optimize-iphone-storage-vs-download-originals", "storage-not-freeing-after-deleting-photos"],
    swipeo="Swipeo cleans the library the system shows. If iCloud Photos is on, what you delete there is deleted in iCloud as well, after the 30-day Recently Deleted window.",
)

add(
    slug="optimize-iphone-storage-vs-download-originals",
    title="Optimize iPhone Storage vs Download and Keep Originals",
    description="Optimize keeps small versions on the phone and full files in iCloud. Download and Keep Originals does the opposite. When to pick each.",
    h1="Optimize iPhone Storage vs Download and Keep Originals",
    lead="One saves phone space, the other saves convenience and offline access.",
    answer="<strong>Optimize iPhone Storage</strong> keeps smaller versions on the phone and full-resolution files in iCloud, which frees space. <strong>Download and Keep Originals</strong> stores full-resolution files on the phone, so photos open instantly and offline but use more space.",
    body="""<table><thead><tr><th></th><th>Optimize iPhone Storage</th><th>Download and Keep Originals</th></tr></thead><tbody>
<tr><td>Phone space</td><td>Less</td><td>More</td></tr>
<tr><td>Offline originals</td><td>No: downloaded on demand</td><td>Yes</td></tr>
<tr><td>Needs iCloud space</td><td>Yes, for all originals</td><td>Yes, iCloud still stores them</td></tr>
<tr><td>Best for</td><td>Big libraries, small phones</td><td>Editing offline, large storage</td></tr>
</tbody></table>
<p>Settings → [your name] → iCloud → Photos. On newer iOS versions the Photos settings may also appear under Settings → Apps → Photos.</p>""",
    faqs=[
        ("Does Optimize delete my originals?", "No. Originals remain in iCloud, as long as you have iCloud space."),
        ("Does Optimize free everything?", "Not fully: the device keeps smaller versions."),
    ],
    sources=[APPLE_STORAGE, TOMS_NO_DELETE, MACRUMORS_GUIDE],
    related=["free-up-iphone-storage-without-deleting-photos", "delete-photos-keep-in-icloud"],
    swipeo="Optimize helps with space; cleaning helps with clutter. Swipeo is for the second: removing what you do not want in the first place.",
)

add(
    slug="free-up-iphone-storage-without-deleting-photos",
    title="Free Up iPhone Storage Without Deleting Photos",
    description="Turn on Optimize iPhone Storage, offload unused apps, review large Messages attachments and clear Safari data before deleting any photo.",
    h1="How to free up iPhone storage without deleting photos",
    lead="Four settings that can give back gigabytes without touching a single memory.",
    answer="Turn on <strong>Optimize iPhone Storage</strong> for iCloud Photos, <strong>offload unused apps</strong> (data is kept), <strong>review large Messages attachments</strong> and clear <strong>Safari</strong> website data. None of these delete your photos.",
    steps=[
        "Settings → [your name] → iCloud → Photos → <strong>Optimize iPhone Storage</strong>.",
        "Settings → General → iPhone Storage → <strong>Offload</strong> apps you rarely use.",
        "iPhone Storage → Messages → <strong>Review Large Attachments</strong>.",
        "Settings → Apps → Safari → Clear History and Website Data (menu path varies by iOS version).",
    ],
    body="<p>Optimize depends on iCloud space, and it is not a replacement for a backup. If these steps are not enough, the next options are deleting <a href=\"../../delete/delete-large-videos-iphone/\">large videos</a> and <a href=\"../../delete/delete-all-screenshots-iphone/\">screenshots</a>.</p>",
    faqs=[
        ("What frees the most space without deleting photos?", "Optimize iPhone Storage can free the most when you have a large library and enough iCloud space."),
        ("Does offloading an app delete its data?", "No. Offloading removes the app but keeps documents and data."),
    ],
    sources=[TOMS_NO_DELETE, APPLE_STORAGE, MACRUMORS_ATTACH],
    related=["optimize-iphone-storage-vs-download-originals", "iphone-storage-full-photos", "delete-large-attachments-messages-iphone"],
    swipeo="When settings are not enough, cleaning the clutter is the next step. " + SW_SWIPE,
)

# ---------------------------------------------------------------- guides

add(
    group="guides",
    slug="declutter-iphone-photo-library",
    title="How to Declutter a Huge iPhone Photo Library (20,000+ Photos)",
    description="A realistic plan for 20,000 photos: remove junk first, work by month in short sessions, mark favorites, then organize what remains.",
    h1="How to declutter a huge iPhone photo library",
    lead="Clean first, organize second, and work in small time-boxed sessions.",
    answer="Start with the obvious junk (<strong>screenshots, duplicates, bursts, accidental shots</strong>), then go <strong>month by month</strong> in short sessions, mark keepers with a <strong>heart</strong>, and only then organize albums. Reviewing around 30 photos a minute means 1,000 photos take about half an hour.",
    steps=[
        "Delete screenshots and screen recordings you no longer need.",
        "Merge exact duplicates and trim bursts.",
        "Go through months one at a time. Stop after a set time.",
        "Heart your best photos so they are easy to find.",
        "Create a few albums for what remains (family, trips).",
        "Empty Recently Deleted.",
    ],
    body="<p>Cleaning first matters: organizing a library full of junk only hides the junk. Face and place grouping in Photos then does most of the organizing for you.</p>",
    faqs=[
        ("How long does it take to clean 20,000 photos?", "At roughly 30 photos a minute, about 11 hours total. Splitting it into 20-minute sessions makes it doable."),
        ("What should I delete first?", "Screenshots, duplicates and bursts: highest clutter, lowest regret."),
    ],
    sources=[IDB_ORGANIZE, ("MacPaw: Organize photos on iPhone", "https://macpaw.com/how-to/organize-photos-on-iphone"), MACPAW_SIMILAR],
    related=["organize-iphone-photos-by-month", "iphone-photo-cleanup-checklist", "swipe-to-delete-photos-iphone"],
    swipeo="Swipeo is built for this pass: review sets (screenshots, bursts, Live Photos, large videos, on this day), swipe through them, and carry on where you stopped. " + SW_SWIPE,
)

add(
    group="guides",
    slug="organize-iphone-photos-by-month",
    title="Clean Your iPhone Photos Month by Month",
    description="Cleaning one month at a time keeps a huge library manageable. How to start, how long a session takes and how to track progress.",
    h1="How to clean your iPhone photos month by month",
    lead="One month at a time turns an impossible job into a routine.",
    answer="Pick one month, open it in Photos' <strong>Months</strong> view, delete the junk, heart the keepers, then stop. Repeat next session. A time-box (for example 15 minutes) keeps it light and consistent.",
    steps=[
        "Photos → Library → <strong>Months</strong>.",
        "Open one month and tap Select.",
        "Delete blurry, duplicate and accidental shots; heart the best.",
        "Note the month you finished so you can continue next time.",
    ],
    body="<p>Working by period keeps context fresh: you remember what happened that month, so decisions are quicker and less emotional.</p>",
    faqs=[
        ("Should I start with the oldest or newest month?", "Newest is easier because you remember it. Oldest often has the biggest clutter. Either works if you stay consistent."),
        ("Is there an automatic way?", "Apps with a Continue where you left feature help. Photos itself does not track your progress."),
    ],
    sources=[IDB_ORGANIZE, ("Apple Support: View photos and videos on iPhone", "https://support.apple.com/guide/iphone/iph3d267610/ios"), ("MacPaw: Organize photos on iPhone", "https://macpaw.com/how-to/organize-photos-on-iphone")],
    related=["declutter-iphone-photo-library", "iphone-photo-cleanup-checklist"],
    swipeo="Swipeo has a <em>Continue where you left</em> list and an <em>On this day</em> set, so you can pick up a cleaning session where it stopped.",
)

add(
    group="guides",
    slug="best-swipe-photo-cleaner-apps-iphone",
    title="Swipe Photo Cleaner Apps for iPhone: What They Do Differently",
    description="A factual look at swipe-to-delete photo cleaners on the App Store: how they work, what to compare, and where Swipeo fits. Dated, with sources.",
    h1="Swipe photo cleaner apps for iPhone compared",
    lead="Many apps use the same swipe idea. These are the differences worth checking.",
    answer="Swipe cleaners show one photo at a time: <strong>swipe to keep or delete</strong>. They differ in <strong>trash or undo</strong>, <strong>sorting (by month or category)</strong>, <strong>free limits</strong> and <strong>privacy</strong>. Facts below come from each App Store listing as of 21 Nov 2026 and may change.",
    body="""<table><thead><tr><th>App (listing)</th><th>What the listing says</th></tr></thead><tbody>
<tr><td>Swipewipe: Photo Cleaner (MWM)</td><td>Swipe-style camera roll cleanup; free with in-app purchases</td></tr>
<tr><td>Clean Camera Roll</td><td>Swipe to delete; shows storage freed per deletion; left deletes, right keeps</td></tr>
<tr><td>Swipy: Photo Delete Swipe</td><td>Photos and videos; free with in-app purchases; iOS 16 or later</td></tr>
<tr><td>Camera Roll Cleaner (Wyprr)</td><td>Adds a trash review step before permanent deletion</td></tr>
<tr><td>Photo Delete Swipe: Swiper</td><td>Swiped-away photos go to a trash area before final deletion</td></tr>
<tr><td>Photo Cleaner: SwipeAway</td><td>Left to delete, right to keep; month-by-month timeline</td></tr>
<tr><td>Swipeo</td><td>Swipe or tap to keep or delete; in-app trash; duplicate groups (not AI); review sets such as screenshots, bursts, Live Photos and large videos; free daily limit, Premium removes it</td></tr>
</tbody></table>
<h2>How to choose</h2>
<ul><li>Pick an app with a <strong>trash or undo</strong>.</li><li>Read the <strong>privacy label</strong> and check what happens with photo access.</li><li>Check the <strong>free limit</strong> so you are not surprised mid-session.</li><li>Look at recent reviews and update dates: many listings are new with similar names.</li></ul>
<p>We make Swipeo, so weigh our row accordingly. Facts in other rows are only what the listings say; we did not test those apps.</p>""",
    faqs=[
        ("Which swipe cleaner is the best?", "There is no neutral winner. Compare trash, privacy, limits and price against your needs."),
        ("Do swipe apps delete permanently?", "Safer ones hold items in a trash first. After that, iOS keeps deleted photos in Recently Deleted for 30 days."),
        ("Is Swipeo free?", "It has a free tier with a daily limit on deletions; Premium removes the limit."),
    ],
    sources=[APPSTORE_SWIPEWIPE, APPSTORE_CLEANCAMERA, APPSTORE_SWIPY, APPSTORE_WYPRR, APPSTORE_SWIPER, APPSTORE_SWIPEAWAY, APPSTORE_SWIPEO],
    related=["swipe-to-delete-photos-iphone", "are-photo-cleaner-apps-safe"],
    swipeo="You are reading a page by the developer of Swipeo. The app is free to start with a daily deletion limit.",
)

add(
    group="guides",
    slug="are-photo-cleaner-apps-safe",
    title="Are iPhone Photo Cleaner Apps Safe? What to Check First",
    description="Cleaner apps ask for access to your whole library. How to read the privacy label, limit photo access and keep deleted photos recoverable.",
    h1="Are iPhone photo cleaner apps safe?",
    lead="Safe depends on the app. Check these five things before you grant access.",
    answer="App Store listings are developer claims, not audits. Before using a cleaner, read the <strong>privacy label</strong>, prefer apps that say photos are <strong>processed on the device</strong>, think about <strong>Limited Photos access</strong>, and make sure there is a <strong>trash or undo</strong> before deletion.",
    steps=[
        "Open the App Store page and read <strong>App Privacy</strong>: look for data used to track you or linked to you.",
        "Prefer apps that state on-device processing, and verify it in the privacy policy.",
        "When iOS asks for photo access, consider Limited Access if you only want to clean part of the library.",
        "Check there is a trash or undo step, and that Recently Deleted still applies.",
        "Compare the pricing for full access before trusting a free trial.",
    ],
    body="<p>One review of a popular cleaner asks why the app sends metadata to its servers, which shows why the claim \"offline\" should be checked rather than assumed. Paying for access does not by itself prove privacy.</p>",
    faqs=[
        ("Can a cleaner app delete photos by mistake?", "Any app with delete access can. Prefer ones with an in-app trash and keep Recently Deleted in mind."),
        ("Do I need to give full photo access?", "Cleaning the whole library needs it. You can start with Limited Access on a few photos."),
    ],
    sources=[APPSTORE_CLEANMYPHONE, ("App Store: Cleanup: Phone Storage Cleaner", "https://apps.apple.com/app/1510944943"), ("Apple Support: Delete photos", "https://support.apple.com/104967")],
    related=["best-swipe-photo-cleaner-apps-iphone", "swipe-to-delete-photos-iphone"],
    swipeo="Swipeo uses the system Photos library on your device and holds deleted items in its own trash first. Read the App Store privacy label and decide for yourself.",
)

add(
    group="guides",
    slug="iphone-photo-cleanup-checklist",
    title="iPhone Photo Cleanup Checklist: What to Delete First",
    description="A prioritized checklist: screenshots, screen recordings, duplicates, bursts, large videos, then Recently Deleted. Highest space gain first.",
    h1="iPhone photo cleanup checklist: what to delete first",
    lead="Highest clutter and lowest regret first, so the first 15 minutes already help.",
    answer="Delete in this order: <strong>screenshots, screen recordings, duplicates, bursts, large videos</strong>, then <strong>empty Recently Deleted</strong>. Check iCloud Photos before you start, because deleting there deletes everywhere.",
    steps=[
        "Check Settings → [your name] → iCloud → Photos (on means deletes sync everywhere).",
        "Albums → Media Types → <strong>Screenshots</strong>: delete.",
        "Media Types → <strong>Screen Recordings</strong>: delete.",
        "Utilities → <strong>Duplicates</strong>: Merge.",
        "Media Types → <strong>Bursts</strong>: keep only favorites.",
        "Media Types → <strong>Videos</strong>: delete long ones you do not need.",
        "Utilities → <strong>Recently Deleted</strong>: Delete All.",
    ],
    body="""<table><thead><tr><th>Step</th><th>Guide</th></tr></thead><tbody>
<tr><td>Screenshots</td><td><a href="../../delete/delete-all-screenshots-iphone/">Delete all screenshots</a></td></tr>
<tr><td>Duplicates</td><td><a href="../../delete/delete-duplicate-photos-iphone/">Delete duplicates</a></td></tr>
<tr><td>Bursts</td><td><a href="../../delete/delete-burst-photos-iphone/">Delete burst photos</a></td></tr>
<tr><td>Large videos</td><td><a href="../../delete/delete-large-videos-iphone/">Delete large videos</a></td></tr>
<tr><td>Recently Deleted</td><td><a href="../../storage/empty-recently-deleted-iphone/">Empty it</a></td></tr>
</tbody></table>""",
    faqs=[
        ("Which step frees the most space?", "Usually large videos, then duplicates and bursts. It depends on your library."),
        ("How often should I do this?", "Every few months, or monthly for heavy camera users."),
    ],
    sources=[APPLE_STORAGE, MACRUMORS_GUIDE, IDB_ORGANIZE],
    related=["declutter-iphone-photo-library", "organize-iphone-photos-by-month", "empty-recently-deleted-iphone"],
    swipeo="Swipeo's review sets follow this order: screenshots, bursts, Live Photos, large videos and duplicates. " + SW_SWIPE,
)
