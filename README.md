./build-firmware gl-ar300m helloworld  > compile_logs.md 2> >(tee -a compile_logs.md >&2)


grep -n -E "Error|failed" -C 5 compile_log.md

