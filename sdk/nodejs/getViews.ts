// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as materialize from "@pulumi/materialize";
 *
 * const all = pulumi.output(materialize.GetViews());
 * const materializeGetViews = pulumi.output(materialize.GetViews({
 *     databaseName: "materialize",
 * }));
 * const materializeSchema = pulumi.output(materialize.GetViews({
 *     databaseName: "materialize",
 *     schemaName: "schema",
 * }));
 * ```
 */
export function getViews(args?: GetViewsArgs, opts?: pulumi.InvokeOptions): Promise<GetViewsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("materialize:index/getViews:GetViews", {
        "databaseName": args.databaseName,
        "schemaName": args.schemaName,
    }, opts);
}

/**
 * A collection of arguments for invoking GetViews.
 */
export interface GetViewsArgs {
    /**
     * Limit views to a specific database
     */
    databaseName?: string;
    /**
     * Limit views to a specific schema within a specific database
     */
    schemaName?: string;
}

/**
 * A collection of values returned by GetViews.
 */
export interface GetViewsResult {
    /**
     * Limit views to a specific database
     */
    readonly databaseName?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Limit views to a specific schema within a specific database
     */
    readonly schemaName?: string;
    /**
     * The views in the account
     */
    readonly views: outputs.GetViewsView[];
}

export function getViewsOutput(args?: GetViewsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetViewsResult> {
    return pulumi.output(args).apply(a => getViews(a, opts))
}

/**
 * A collection of arguments for invoking GetViews.
 */
export interface GetViewsOutputArgs {
    /**
     * Limit views to a specific database
     */
    databaseName?: pulumi.Input<string>;
    /**
     * Limit views to a specific schema within a specific database
     */
    schemaName?: pulumi.Input<string>;
}