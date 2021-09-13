#!/usr/bin/env sh

# Ref:
# * https://github.com/tiangolo/uwsgi-nginx-docker/issues/61#issuecomment-508034634
# * https://gist.github.com/ReallyLiri/f833510d350b242ff89b9b76fdf21ea5
# * https://serverfault.com/a/922943
# * https://gist.github.com/tomazzaman/63265dfab3a9a61781993212fa1057cb
# * https://gist.github.com/tomazzaman/63265dfab3a9a61781993212fa1057cb#gistcomment-2812931
# * https://github.com/Supervisor/supervisor/issues/733
# * 
printf "READY\n";

while read line; do
  echo "Processing Event: $line" >&2;
  kill $PPID
done < /dev/stdin
