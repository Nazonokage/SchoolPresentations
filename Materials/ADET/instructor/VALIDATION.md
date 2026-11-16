# Validation record · 4 November 2026

All 20 lesson screens and the additional M05 route passed strict TypeScript checking against the installed SDK 58 mobile project. From examples/mobile run `node check-all.mjs` after changing an example. The working shell was returned to M01.

Metro produced Android Hermes bundles for the introductory screen, Expo Router example and audio example. The audio bundle contained the supplied WAV. This checks module resolution, routing entry configuration and packaging. It does not demonstrate a successful camera session, permission prompt, notification delivery, playback or physical-device LAN connection.

The Node/Express API was executed against a disposable MongoDB 8.3 instance bound to loopback. Valid creation, rejection of blank input, strict Boolean patch validation, update/read, deletion, missing-record handling and the suggestion endpoint passed. The FastAPI/SQLAlchemy API passed equivalent contract checks using an isolated file-backed SQLite database, including reading after disposing the connection pool. The XAMPP/WampServer MySQL/MariaDB path is supplied with setup instructions and still needs a live test with the classroom database and credentials.

The supplied screen pictures are original SVG illustrations of expected states. Five pinned external asset URLs returned HTTP 200 with SVG content and were saved locally alongside the project license. Classroom timing and behavior on students’ exact Expo Go versions remain unverified.

**Before the first meeting** select M01, run it on the instructor phone, and compare the screen with the module. Before Midterm, test phone → selected API → database and a restart. Before Pre-final, test allow, deny and cancel on supported physical devices. Use development builds when a chosen native feature requires one.

This project is for local teaching. The package install reported five moderate audit findings at installation. Review current dependency advisories and release settings separately before distributing a production binary.
