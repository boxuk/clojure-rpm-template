
# Clojure RPM's Via Leiningen

This repository contains template code for building an RPM for a
[Clojure](http://clojure.org) application using 
[Leiningen](http://leiningen.org).

The specfile is customized slightly to Box UK's packaging process (it
assumes the source tarball is placed in the build root), but should be a decent
starting point for anyone looking to develop their own packaging process.

## Assumptions

The [specfile](application.spec) uses Leiningen and the 
[lein-bin](https://github.com/Raynes/lein-bin) plugin to build a standalone 
"binary" for the application, that can then be started and stopped via the 
[init script](sources/chkconfig.conf).

