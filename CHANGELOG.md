CHANGELOG
=========
## 0.3.20 2025-08-04
Upgrade to Terraform Provider [0.8.20](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.20).

## 0.3.19 2025-07-29
Upgrade to Terraform Provider [0.8.19](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.19).

## 0.3.18 2025-06-20
Upgrade to Terraform Provider [0.8.18](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.18).

## 0.3.17 2025-06-03
Upgrade to Terraform Provider [0.8.17](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.17).

## 0.3.16 2025-04-03
Upgrade to Terraform Provider [0.8.16](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.16).

## 0.3.15 2025-02-27
Upgrade to Terraform Provider [0.8.15](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.15).

## 0.3.14 2025-02-24
Upgrade to latest Pulumi SDK (`v3.152.0`) and Pulumi Terraform Bridge (`v3.103.0`).

## 0.3.13 2025-01-21
Update to Terraform Provider [0.8.13](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.13).

## 0.3.12 2024-12-23
Update to Terraform Provider [0.8.12](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.12).

## 0.3.11 2024-11-21
Update to Terraform Provider [0.8.11](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.11).

## 0.3.10 2024-10-07
Update to Terraform Provider [0.8.10](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.10).

## 0.3.9 2024-09-30
Update to Terraform Provider [0.8.9](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.9).

## 0.3.8 2024-08-26
Update to Terraform Provider [0.8.8](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.8).

## 0.3.7 2024-08-15
Update to Terraform Provider [0.8.7](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.7).

## 0.3.6 2024-07-31
Update to Terraform Provider [0.8.6](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.6).

## 0.3.5 2024-07-23
Update to Terraform Provider [0.8.5](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.5).

## 0.3.4 - 2024-07-16
Update to Terraform Provider [0.8.4](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.4).

## 0.3.3 - 2024-07-08
Update to Terraform Provider [0.8.3](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.3).

## 0.3.2 - 2024-07-01
Update to Terraform Provider [0.8.2](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.2).

## 0.3.1 - 2024-06-20
Update to Terraform Provider [0.8.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.1).

## 0.3.0 - 2024-05-16
Update to Terraform Provider [0.8.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.8.0).

## 0.2.1 - 2024-04-30
Update to Terraform Provider [0.7.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.7.1).

## 0.2.0 - 2024-04-25
Update to Terraform Provider [0.7.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.7.0).

## 0.1.10 - 2024-04-01
Update to Terraform Provider [0.6.10](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.10).

## 0.1.9 - 2024-03-29
Update to Terraform Provider [0.6.9](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.9).

## 0.1.8 - 2024-03-14
Update to Terraform Provider [0.6.8](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.8).

## 0.1.7 - 2024-03-11
Update to Terraform Provider [0.6.7](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.7).

## 0.1.6 - 2024-02-29
Update to Terraform Provider [0.6.6](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.6).

## 0.1.5 - 2024-02-19
Update to Terraform Provider [0.6.5](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.5).

## 0.1.4 - 2024-02-03
Update to Terraform Provider [0.6.4](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.4).

## 0.1.3 - 2024-02-02
Update to Terraform Provider [0.6.3](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.3).

## 0.1.2 - 2024-02-01
Update to Terraform Provider [0.6.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.1).

## 0.1.1 - 2024-01-23
Update to Terraform Provider [0.6.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.6.0).

### Breaking Changes
* Drop `SIZE` support for sources and sinks.

## 0.1.0 - 2024-01-11
Update to Terraform Provider [0.5.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.5.0).

### Breaking Changes
* **Provider Configuration Changes**:
  * Deprecated the `host`, `port`, and `user` parameters in the provider configuration. These details are now derived from the app password.
  * Retained only the `password` definition in the provider configuration. This password is used to fetch all necessary connection information.
* **New `region` Configuration**:
  * Introduced a new `default_region` parameter in the provider configuration. This allows users to specify the default region for resource creation.
  * The `default_region` parameter can be overridden in specific resource configurations if a particular resource needs to be created in a non-default region.

### Migration Guide
* Before upgrading to `v0.1.0`, users should ensure that they have upgraded to `v0.0.8` which introduced a state migration necessary for `v0.1.0`. After upgrading to `v0.0.0`, users should run `pulumi refresh` to ensure that the state migration has completed successfully.

## 0.0.8 - 2023-12-14
Update to Terraform Provider [0.4.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.4.1).

## 0.0.7 - 2023-12-06
Update to Terraform Provider [0.3.4](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.4).

## 0.0.6 - 2023-11-30
Update to Terraform Provider [0.3.3](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.3).

## 0.0.5 - 2023-11-26
Fix issues with the Terraform Bridge in v0.0.4.

## 0.0.4 - 2023-11-23
Update to Terraform Provider [0.3.1](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.1).

## 0.0.3 - 2023-11-17
Update to Terraform Provider [0.3.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.3.0).

## 0.0.2 - 2023-10-31
Update to Terraform Provider [0.2.0](https://github.com/MaterializeInc/terraform-provider-materialize/releases/tag/v0.2.0).

## 0.0.1 - 2023-10-02
Initial release.
