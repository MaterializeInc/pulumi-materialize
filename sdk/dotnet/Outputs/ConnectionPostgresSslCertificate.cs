// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Materialize.Outputs
{

    [OutputType]
    public sealed class ConnectionPostgresSslCertificate
    {
        /// <summary>
        /// The ssl*certificate secret value.
        /// </summary>
        public readonly Outputs.ConnectionPostgresSslCertificateSecret? Secret;
        /// <summary>
        /// The ssl_certificate text value.
        /// </summary>
        public readonly string? Text;

        [OutputConstructor]
        private ConnectionPostgresSslCertificate(
            Outputs.ConnectionPostgresSslCertificateSecret? secret,

            string? text)
        {
            Secret = secret;
            Text = text;
        }
    }
}