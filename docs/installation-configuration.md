---
title: Materialize Installation & Configuration
meta_desc: Provides an overview on how to configure credentials for the Materialize provider.
layout: package
---

## Installation

The Pulumi Materialize provider is available as a package in all Pulumi languages:

* Python: [`pulumi_materialize`](https://pypi.org/project/pulumi-materialize/)

## Setup

To provision resources with the Pulumi Materialize provider, you need to have Materialize credentials. 

## Configuration Options

Use `pulumi config set materialize:<option>`.

| Option | Required/Optional | Description |
|-----|------|----|
| `host`| Required | Materialize host
| `user`| Required | Materialize user |
| `password`| Required | Materialize password |
| `port`| Optional | The Materialize port number to connect to at the server host |
| `database`| Optional | Materialize database |