Build command:

    mv .idea ../; gbp buildpackage --git-ignore-new; mv ../.idea ./

Clean command:

    rm -rf .pybuild/ debian/.debhelper debian/debhelper-build-stamp debian/python3-http-relay src/http_relay.egg-info ../http-relay_2.* debian/tmp debian/*.substvars debian/*.debhelper debian/http-relay debian/http-relay.1 debian/*.log