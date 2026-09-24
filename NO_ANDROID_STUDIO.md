# Build Aldurra v2 without Android Studio

You do not need Android Studio for the test APK.

## Easiest method: GitHub Actions

1. Create a new GitHub repository.
2. Upload **the contents of this project folder** to the repository root. The `.github` folder must also be uploaded.
3. Open the repository's **Actions** tab.
4. Select **Build Aldurra Android APK**.
5. Choose **Run workflow**.
6. When the build finishes, open the completed workflow run.
7. Under **Artifacts**, download **Aldurra-v2-APK**.
8. Unzip it. The installable file is `Aldurra-v2-test.apk`.

The workflow first executes `verify_content.py`. The build stops if the locked chapter names, page list, or approved page image hashes do not match the Aldurra v2 content manifest.

## Important: test APK vs Play Store release

`Aldurra-v2-test.apk` is signed automatically with Android's debug signing key. It is suitable for testing on an Android phone.

It is **not** the Play Store production update. A production update must be signed with the correct existing Aldurra upload/signing identity. Do not create a random replacement key if the existing app is already published.

If the old Aldurra APK on your phone was signed with a different key, Android may refuse to install the test APK over it. For testing only, uninstall the old app first, then install `Aldurra-v2-test.apk`.
