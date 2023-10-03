# Contributing

## Developing the provider

The Pulumi provider is dependent on the [Terraform provider](https://github.com/MaterializeInc/terraform-provider-materialize). Any new features or changes should be applied there.

### Updating Terraform provider

To update the Terraform provider, change the version of `github.com/MaterializeInc/terraform-provider-materialize`in the [provider/go.mod](provider/go.mod) and run `go mod tidy`.

> **Note**
The repo is configured with dependabot to check for new versions of the Terraform provider.

### Updating the schema

To update the schema for the Pulumi provider (after the Terraform version has been updated) run `make tfgen` to automatically generate any new schema or property changes.

If a new resource or data source has been added, the reference will need to be added to [provider/resources.go]. After it has been added, you can run `make tfgen`.

## Cutting a release

To cut a new release of the provider, create a new tag and push that tag. This will trigger a Github Action to generate the artifacts and build the configured SDKs.

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

[Materialize]: https://materialize.com