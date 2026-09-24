# Aldurra v2 Android

Native offline Android rebuild preserving the original Aldurra package ID and exact recovered chapter titles/page assets.

## Content integrity rule
- `app/src/main/assets/pages_manifest.json` is the source of truth for chapter names.
- Do not replace chapter titles with generic labels such as "الفصل الأول".
- Page images are enhanced non-generatively from the original APK and are not rewritten.
- Chapter 6 has no `ch6_010.jpg` in the original APK; the manifest intentionally lists only existing pages.

## Build
Use current Android Studio with Android SDK 36 installed.
This project uses Android Gradle Plugin 9.4.0, Java 17, compileSdk/targetSdk 36.

For a local debug APK:

    gradle :app:assembleDebug

For a release bundle:

    gradle :app:bundleRelease

If Aldurra is already published, sign the production release with the original Play upload/signing lineage. The package ID is preserved as:
`io.kodular.ahmed_mos_hus.Aldurra`

## Privacy/security
No Internet permission, no storage permission, no ads, analytics, trackers, WebView, or remote code.
