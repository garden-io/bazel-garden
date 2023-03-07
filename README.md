# Deploying a bazel project via Garden
This project shows how to build a python app with bazel and deploy it with Garden.
It has two environments a local one that deploys to a local kubernetes cluster and a remote one that is configured to deploy to a cluster in GCP and push images to a Google Container Registry.

This is a work in progress proof-of-concept and we are very happy to receive feedback on this!

# Limitations
- Garden version hash might not update if one of the bazel dependencies change. For example, if the calculator library changes, `garden deploy` will not re-deploy since the image tag did not change.
- No dev-mode / code syncing

# Prerequisites:
- Docker Desktop
- `brew install bazelisk`

# What works
- `garden test` (will run tests both in kubernetes and locally using bazel + exec-module)
- `garden deploy`

# Open questions
- How to enable Dev mode?
- Is there another way to leverage remote building (Passing .tar from bazel to buildkit via garden or similar, since packaging a tar doesn't need docker daemon)?
- Is there a better way to integrate garden + bazel?
  - One improvement might be that we use the `publish_container` rule in bazel instead of the `bazel run` hack
  - A completely different appraoch that might be worth investigation is writing Bazel rulesets for Garden
