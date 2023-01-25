We can use this approach locally since docker daemon is required for building the image (and pushing to local registry) via bazel.

Pre-requisites:
- Docker Desktop

Steps to run:
- `brew install bazelisk`
- `garden deploy`

Open questions:
- How can we get the output project files and pass them to docker build as args (Cannot pass directly via COPY, since docker build ignores symlinks)?
- Is there another way to leverage remote building (Passing .tar from bazel to buildkit via garden or similar, since packaging a tar doesn't need docker daemon)?
- How can we use dev mode?
