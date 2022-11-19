using System.Security.Cryptography.X509Certificates;
using System.Security.Permissions;
using EsiaNET.AspNetCore.Authentication;

namespace GosUslugiApi.EsiaAuth;

public  class SignProviderGenerator: IDisposable
{
    private  readonly X509Store _storage;
    private static  X509Certificate2Collection _certificateCollection;
    
    public SignProviderGenerator(StoreName name, StoreLocation storeLocation)
    {
        _storage = new X509Store(name, storeLocation);
    }

    public  SignProviderGenerator()
    {
        _storage = new X509Store(StoreName.My, StoreLocation.LocalMachine);
        SetCertificateCollections();
    }

    public static X509Certificate2 GetCertificate2() => _certificateCollection[0];

    private void SetCertificateCollections()
    {
        try
        {
            _storage.Open(OpenFlags.OpenExistingOnly);
            _certificateCollection = _storage.Certificates
                .Find(X509FindType.FindBySerialNumber, "SERIAL_ID", false);
        }
        catch (Exception e)
        {
            // There will logging in a future
            Console.WriteLine(e);
            throw;
        }
        finally
        {
            _storage.Close();
        }
    }
    
    public void Dispose()
    {
        _storage.Dispose();
    }
}