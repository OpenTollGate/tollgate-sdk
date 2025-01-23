Yes, that's exactly the issue. The error messages also indicate there are problems with the Makefiles:

```
ERROR: please fix feeds/custom/lang/golang/golang/Makefile - see logs/feeds/custom/lang/golang/golang/dump.txt for details
ERROR: please fix feeds/custom/tollgate-module-relay-go/Makefile - see logs/feeds/custom/tollgate-module-relay-go/dump.txt for details
```

To resolve this:

1. First, check the error details in the log files:
```bash
cat logs/feeds/custom/lang/golang/golang/dump.txt
cat logs/feeds/custom/tollgate-module-relay-go/dump.txt
```

2. You'll need to uninstall the existing golang package and prevent it from being automatically installed:
```bash
./scripts/feeds uninstall golang
rm -rf package/feeds/packages/golang
```

3. Then modify your feeds.conf to prioritize your custom feed:
```bash
# Edit feeds.conf to move custom feed to top
src-git custom https://github.com/OpenTollGate/custom-nostr-feed.git;main
# Other feeds below...
```

4. Clean and update feeds again:
```bash
./scripts/feeds clean
./scripts/feeds update -a
./scripts/feeds install -p custom golang
```

5. If you're still having issues, you might need to rename your golang package in your custom feed to avoid conflicts, for example:
```bash
mv feeds/custom/lang/golang feeds/custom/lang/golang-custom
# Update the corresponding Makefile to use the new name
```

Can you share the contents of the dump.txt files? This will help identify the specific issues with the Makefiles that need to be fixed.