// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize
{
    /// <summary>
    /// A sink describes an external system you want Materialize to write data to, and provides details about how to encode that data.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Materialize = Pulumi.Materialize;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleSinkKafka = new Materialize.SinkKafka("exampleSinkKafka", new()
    ///     {
    ///         Envelope = new Materialize.Inputs.SinkKafkaEnvelopeArgs
    ///         {
    ///             Upsert = true,
    ///         },
    ///         Format = new Materialize.Inputs.SinkKafkaFormatArgs
    ///         {
    ///             Avro = new Materialize.Inputs.SinkKafkaFormatAvroArgs
    ///             {
    ///                 SchemaRegistryConnection = new Materialize.Inputs.SinkKafkaFormatAvroSchemaRegistryConnectionArgs
    ///                 {
    ///                     DatabaseName = "database",
    ///                     Name = "csr_connection",
    ///                     SchemaName = "schema",
    ///                 },
    ///             },
    ///         },
    ///         From = new Materialize.Inputs.SinkKafkaFromArgs
    ///         {
    ///             Name = "table",
    ///         },
    ///         KafkaConnection = new Materialize.Inputs.SinkKafkaKafkaConnectionArgs
    ///         {
    ///             Name = "kafka_connection",
    ///         },
    ///         SchemaName = "schema",
    ///         Size = "3xsmall",
    ///         Topic = "test_avro_topic",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// # Sinks can be imported using the sink id
    /// 
    /// ```sh
    ///  $ pulumi import materialize:index/sinkKafka:SinkKafka example_sink_kafka &lt;sink_id&gt;
    /// ```
    /// </summary>
    [MaterializeResourceType("materialize:index/sinkKafka:SinkKafka")]
    public partial class SinkKafka : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The cluster to maintain this sink. If not specified, the size option must be specified.
        /// </summary>
        [Output("clusterName")]
        public Output<string> ClusterName { get; private set; } = null!;

        /// <summary>
        /// The identifier for the sink database.
        /// </summary>
        [Output("databaseName")]
        public Output<string?> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// How to interpret records (e.g. Debezium, Upsert).
        /// </summary>
        [Output("envelope")]
        public Output<Outputs.SinkKafkaEnvelope?> Envelope { get; private set; } = null!;

        /// <summary>
        /// How to decode raw bytes from different formats into data structures it can understand at runtime.
        /// </summary>
        [Output("format")]
        public Output<Outputs.SinkKafkaFormat?> Format { get; private set; } = null!;

        /// <summary>
        /// The name of the source, table or materialized view you want to send to the sink.
        /// </summary>
        [Output("from")]
        public Output<Outputs.SinkKafkaFrom> From { get; private set; } = null!;

        /// <summary>
        /// The name of the Kafka connection to use in the sink.
        /// </summary>
        [Output("kafkaConnection")]
        public Output<Outputs.SinkKafkaKafkaConnection> KafkaConnection { get; private set; } = null!;

        /// <summary>
        /// An optional list of columns to use for the Kafka key. If unspecified, the Kafka key is left unset.
        /// </summary>
        [Output("keys")]
        public Output<ImmutableArray<string>> Keys { get; private set; } = null!;

        /// <summary>
        /// The identifier for the sink.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The fully qualified name of the sink.
        /// </summary>
        [Output("qualifiedSqlName")]
        public Output<string> QualifiedSqlName { get; private set; } = null!;

        /// <summary>
        /// The identifier for the sink schema.
        /// </summary>
        [Output("schemaName")]
        public Output<string?> SchemaName { get; private set; } = null!;

        /// <summary>
        /// The type of sink.
        /// </summary>
        [Output("sinkType")]
        public Output<string> SinkType { get; private set; } = null!;

        /// <summary>
        /// The size of the sink.
        /// </summary>
        [Output("size")]
        public Output<string> Size { get; private set; } = null!;

        /// <summary>
        /// Whether to emit the consolidated results of the query before the sink was created at the start of the sink.
        /// </summary>
        [Output("snapshot")]
        public Output<bool?> Snapshot { get; private set; } = null!;

        /// <summary>
        /// The Kafka topic you want to subscribe to.
        /// </summary>
        [Output("topic")]
        public Output<string> Topic { get; private set; } = null!;


        /// <summary>
        /// Create a SinkKafka resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SinkKafka(string name, SinkKafkaArgs args, CustomResourceOptions? options = null)
            : base("materialize:index/sinkKafka:SinkKafka", name, args ?? new SinkKafkaArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SinkKafka(string name, Input<string> id, SinkKafkaState? state = null, CustomResourceOptions? options = null)
            : base("materialize:index/sinkKafka:SinkKafka", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/MaterializeInc/pulumi-materialize",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SinkKafka resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SinkKafka Get(string name, Input<string> id, SinkKafkaState? state = null, CustomResourceOptions? options = null)
        {
            return new SinkKafka(name, id, state, options);
        }
    }

    public sealed class SinkKafkaArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The cluster to maintain this sink. If not specified, the size option must be specified.
        /// </summary>
        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        /// <summary>
        /// The identifier for the sink database.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// How to interpret records (e.g. Debezium, Upsert).
        /// </summary>
        [Input("envelope")]
        public Input<Inputs.SinkKafkaEnvelopeArgs>? Envelope { get; set; }

        /// <summary>
        /// How to decode raw bytes from different formats into data structures it can understand at runtime.
        /// </summary>
        [Input("format")]
        public Input<Inputs.SinkKafkaFormatArgs>? Format { get; set; }

        /// <summary>
        /// The name of the source, table or materialized view you want to send to the sink.
        /// </summary>
        [Input("from", required: true)]
        public Input<Inputs.SinkKafkaFromArgs> From { get; set; } = null!;

        /// <summary>
        /// The name of the Kafka connection to use in the sink.
        /// </summary>
        [Input("kafkaConnection", required: true)]
        public Input<Inputs.SinkKafkaKafkaConnectionArgs> KafkaConnection { get; set; } = null!;

        [Input("keys")]
        private InputList<string>? _keys;

        /// <summary>
        /// An optional list of columns to use for the Kafka key. If unspecified, the Kafka key is left unset.
        /// </summary>
        public InputList<string> Keys
        {
            get => _keys ?? (_keys = new InputList<string>());
            set => _keys = value;
        }

        /// <summary>
        /// The identifier for the sink.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The identifier for the sink schema.
        /// </summary>
        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        /// <summary>
        /// The size of the sink.
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// Whether to emit the consolidated results of the query before the sink was created at the start of the sink.
        /// </summary>
        [Input("snapshot")]
        public Input<bool>? Snapshot { get; set; }

        /// <summary>
        /// The Kafka topic you want to subscribe to.
        /// </summary>
        [Input("topic", required: true)]
        public Input<string> Topic { get; set; } = null!;

        public SinkKafkaArgs()
        {
        }
        public static new SinkKafkaArgs Empty => new SinkKafkaArgs();
    }

    public sealed class SinkKafkaState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The cluster to maintain this sink. If not specified, the size option must be specified.
        /// </summary>
        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        /// <summary>
        /// The identifier for the sink database.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// How to interpret records (e.g. Debezium, Upsert).
        /// </summary>
        [Input("envelope")]
        public Input<Inputs.SinkKafkaEnvelopeGetArgs>? Envelope { get; set; }

        /// <summary>
        /// How to decode raw bytes from different formats into data structures it can understand at runtime.
        /// </summary>
        [Input("format")]
        public Input<Inputs.SinkKafkaFormatGetArgs>? Format { get; set; }

        /// <summary>
        /// The name of the source, table or materialized view you want to send to the sink.
        /// </summary>
        [Input("from")]
        public Input<Inputs.SinkKafkaFromGetArgs>? From { get; set; }

        /// <summary>
        /// The name of the Kafka connection to use in the sink.
        /// </summary>
        [Input("kafkaConnection")]
        public Input<Inputs.SinkKafkaKafkaConnectionGetArgs>? KafkaConnection { get; set; }

        [Input("keys")]
        private InputList<string>? _keys;

        /// <summary>
        /// An optional list of columns to use for the Kafka key. If unspecified, the Kafka key is left unset.
        /// </summary>
        public InputList<string> Keys
        {
            get => _keys ?? (_keys = new InputList<string>());
            set => _keys = value;
        }

        /// <summary>
        /// The identifier for the sink.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The fully qualified name of the sink.
        /// </summary>
        [Input("qualifiedSqlName")]
        public Input<string>? QualifiedSqlName { get; set; }

        /// <summary>
        /// The identifier for the sink schema.
        /// </summary>
        [Input("schemaName")]
        public Input<string>? SchemaName { get; set; }

        /// <summary>
        /// The type of sink.
        /// </summary>
        [Input("sinkType")]
        public Input<string>? SinkType { get; set; }

        /// <summary>
        /// The size of the sink.
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// Whether to emit the consolidated results of the query before the sink was created at the start of the sink.
        /// </summary>
        [Input("snapshot")]
        public Input<bool>? Snapshot { get; set; }

        /// <summary>
        /// The Kafka topic you want to subscribe to.
        /// </summary>
        [Input("topic")]
        public Input<string>? Topic { get; set; }

        public SinkKafkaState()
        {
        }
        public static new SinkKafkaState Empty => new SinkKafkaState();
    }
}