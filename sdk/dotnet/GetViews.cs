// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize
{
    public static class GetViews
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Materialize = Pulumi.Materialize;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var all = Materialize.GetViews.Invoke();
        /// 
        ///     var materialize = Materialize.GetViews.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///     });
        /// 
        ///     var materializeSchema = Materialize.GetViews.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///         SchemaName = "schema",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetViewsResult> InvokeAsync(GetViewsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetViewsResult>("materialize:index/getViews:GetViews", args ?? new GetViewsArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Materialize = Pulumi.Materialize;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var all = Materialize.GetViews.Invoke();
        /// 
        ///     var materialize = Materialize.GetViews.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///     });
        /// 
        ///     var materializeSchema = Materialize.GetViews.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///         SchemaName = "schema",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetViewsResult> Invoke(GetViewsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetViewsResult>("materialize:index/getViews:GetViews", args ?? new GetViewsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetViewsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Limit views to a specific database
        /// </summary>
        [Input("databaseName")]
        public string? DatabaseName { get; set; }

        /// <summary>
        /// Limit views to a specific schema within a specific database
        /// </summary>
        [Input("schemaName")]
        public string? SchemaName { get; set; }

        public GetViewsArgs()
        {
        }
        public static new GetViewsArgs Empty => new GetViewsArgs();
    }

    public sealed class GetViewsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Limit views to a specific database
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// Limit views to a specific schema within a specific database
        /// </summary>
        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        public GetViewsInvokeArgs()
        {
        }
        public static new GetViewsInvokeArgs Empty => new GetViewsInvokeArgs();
    }


    [OutputType]
    public sealed class GetViewsResult
    {
        /// <summary>
        /// Limit views to a specific database
        /// </summary>
        public readonly string? DatabaseName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Limit views to a specific schema within a specific database
        /// </summary>
        public readonly string? SchemaName;
        /// <summary>
        /// The views in the account
        /// </summary>
        public readonly ImmutableArray<Outputs.GetViewsViewResult> Views;

        [OutputConstructor]
        private GetViewsResult(
            string? databaseName,

            string id,

            string? schemaName,

            ImmutableArray<Outputs.GetViewsViewResult> views)
        {
            DatabaseName = databaseName;
            Id = id;
            SchemaName = schemaName;
            Views = views;
        }
    }
}