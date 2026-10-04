#!/bin/bash
gradle build --no-daemon --stacktrace > build.log 2>&1
code=$?
if [ $code -ne 0 ]; then
  msg=$(grep -v -E "^\s+at |^$" build.log | tail -n 45 | sed 's/%/%25/g' | sed ':a;N;$!ba;s/\n/%0A/g' | head -c 3800)
  echo "::error title=BUILDLOG::$msg"
fi
exit $code
