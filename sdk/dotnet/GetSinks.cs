// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize
{
    public static class GetSinks
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
        ///     var all = Materialize.GetSinks.Invoke();
        /// 
        ///     var materialize = Materialize.GetSinks.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///     });
        /// 
        ///     var materializeSchema = Materialize.GetSinks.Invoke(new()
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
        public static Task<GetSinksResult> InvokeAsync(GetSinksArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSinksResult>("materialize:index/getSinks:GetSinks", args ?? new GetSinksArgs(), options.WithDefaults());

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
        ///     var all = Materialize.GetSinks.Invoke();
        /// 
        ///     var materialize = Materialize.GetSinks.Invoke(new()
        ///     {
        ///         DatabaseName = "materialize",
        ///     });
        /// 
        ///     var materializeSchema = Materialize.GetSinks.Invoke(new()
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
        public static Output<GetSinksResult> Invoke(GetSinksInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSinksResult>("materialize:index/getSinks:GetSinks", args ?? new GetSinksInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSinksArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Limit sinks to a specific database
        /// </summary>
        [Input("databaseName")]
        public string? DatabaseName { get; set; }

        /// <summary>
        /// Limit sinks to a specific schema within a specific database
        /// </summary>
        [Input("schemaName")]
        public string? SchemaName { get; set; }

        public GetSinksArgs()
        {
        }
        public static new GetSinksArgs Empty => new GetSinksArgs();
    }

    public sealed class GetSinksInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Limit sinks to a specific database
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// Limit sinks to a specific schema within a specific database
        /// </summary>
        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        public GetSinksInvokeArgs()
        {
        }
        public static new GetSinksInvokeArgs Empty => new GetSinksInvokeArgs();
    }


    [OutputType]
    public sealed class GetSinksResult
    {
        /// <summary>
        /// Limit sinks to a specific database
        /// </summary>
        public readonly string? DatabaseName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Limit sinks to a specific schema within a specific database
        /// </summary>
        public readonly string? SchemaName;
        /// <summary>
        /// The sinks in the account
        /// </summary>
        public readonly ImmutableArray<Outputs.GetSinksSinkResult> Sinks;

        [OutputConstructor]
        private GetSinksResult(
            string? databaseName,

            string id,

            string? schemaName,

            ImmutableArray<Outputs.GetSinksSinkResult> sinks)
        {
            DatabaseName = databaseName;
            Id = id;
            SchemaName = schemaName;
            Sinks = sinks;
        }
    }
}