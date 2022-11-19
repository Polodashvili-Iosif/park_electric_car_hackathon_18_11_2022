using System.Security.Cryptography.X509Certificates;
using EsiaNET;
using EsiaNET.AspNetCore.Authentication;
using GosUslugiApi.EsiaAuth.Models;

namespace GosUslugiApi.EsiaAuth.Configuration;

public static class ConfigureEsia
{
    public static IServiceCollection AddEsiaAuth(this IServiceCollection collection, IConfiguration configuration)
    {
        collection.AddOptions<EsiaDataModel>().Bind(configuration.GetSection("EsiaDataModel"));
        collection.AddAuthentication().AddEsia((options =>
        {
            options.ClientId = configuration.GetValue<string>("EsiaDataModel:ClientSystemId");
            options.AuthorizationEndpoint =
                EsiaConsts.EsiaAuthUrl; 
            options.TokenEndpoint =
                EsiaConsts
                    .EsiaTokenUrl;
            string path = configuration.GetValue<string>("EsiaDataModel:CertificatePath");
            options.SignProvider = EsiaAuthenticationOptions
                .CreateSignProvider(SignProviderGenerator.GetCertificate2, 
                    () => new X509Certificate2(path));
            options.VerifyTokenSignature = false; 
            options.SaveTokens =
                true;
            options.Scope.Add("openid");
            options.Scope.Add("fullname");
            options.Scope.Add("id_doc");
            options.RestOptions = new EsiaRestOptions();
            options.Events.OnCreatingTicket = c =>
            {
                var accessToken = c.AccessToken;

                return Task.CompletedTask;
            };
        }));
        return collection;
    }
}