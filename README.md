# Aldurra v2 Android cloud build

This repository is configured to build the modern Aldurra v2 Android app without Android Studio.

## One required upload
Upload `Aldurra_V2_No_Android_Studio_Build_Kit.zip` to the repository root.

The GitHub Action will then:
1. extract the Android project;
2. verify the locked original chapter names and 212 approved pages;
3. install Android SDK 36;
4. build an installable test APK;
5. publish `Aldurra-v2-test.apk` as the `Aldurra-v2-APK` Actions artifact.

The religious/book content remains protected by the project's integrity checker.
