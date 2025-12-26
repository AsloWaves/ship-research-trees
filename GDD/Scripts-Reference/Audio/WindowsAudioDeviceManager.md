# WindowsAudioDeviceManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Audio/WindowsAudioDeviceManager.cs` |
| **Namespace** | `WOS.Audio` |
| **Type** | Static class |
| **Lines** | ~294 |
| **Platform** | Windows Vista+ (WASAPI) |
| **Architecture** | Native COM interop for Windows Core Audio APIs |

## Purpose
Windows-specific audio device manager using Core Audio APIs (WASAPI). Provides enumeration of audio output devices via COM interop. Serves as fallback/reference implementation; FMOD-based solution (`FMODAudioDeviceManager`) is preferred.

---

## AudioDevice Class

```csharp
public class AudioDevice
{
    public string Id { get; set; }           // Windows device ID
    public string FriendlyName { get; set; } // Display name
    public bool IsDefault { get; set; }      // Is system default
}
```

---

## Native Interop

### COM Interfaces
| Interface | GUID | Purpose |
|-----------|------|---------|
| `IMMDeviceEnumerator` | A95664D2-9614-4F35-A746-DE8DB63617E6 | Enumerate audio endpoints |
| `IMMDeviceCollection` | 0BD7A1BE-7A1A-44DB-8397-CC5392387B5E | Collection of devices |
| `IMMDevice` | D666063F-1587-4E43-81F1-B948E807363F | Single audio device |
| `IPropertyStore` | 886d8eeb-8cf2-4446-8d02-cdba1dbdcf99 | Device properties |

### Property Keys
```csharp
// Device friendly name property
PKEY_Device_FriendlyName = new Guid("a45c254e-df1c-4efd-8020-67d146a850e0");
PID_Device_FriendlyName = 14;
```

---

## Public API

### Device Enumeration
```csharp
// Get all active audio output devices
public static List<AudioDevice> GetOutputDevices()

// Set output device (limited - see notes)
public static bool SetOutputDevice(string deviceId)
```

---

## Enumeration Flow

```csharp
public static List<AudioDevice> GetOutputDevices()
{
    // 1. Check platform (Windows only)
    if (platform != WindowsPlayer && platform != WindowsEditor)
        return fallback;

    // 2. Create device enumerator via COM
    CoCreateInstance(CLSID_MMDeviceEnumerator, ...);

    // 3. Get default device ID
    enumerator.GetDefaultAudioEndpoint(eRender, 0, out defaultDevice);

    // 4. Enumerate all active output devices
    enumerator.EnumAudioEndpoints(eRender, DEVICE_STATE_ACTIVE, out collection);

    // 5. For each device, get ID and friendly name
    foreach device:
        device.GetId(out deviceId);
        device.OpenPropertyStore(STGM_READ, out propertyStore);
        propertyStore.GetValue(PKEY_Device_FriendlyName, out name);

    // 6. Release COM objects
    Marshal.ReleaseComObject(...);

    return devices;
}
```

---

## Platform Check

```csharp
// Only works on Windows
if (Application.platform != RuntimePlatform.WindowsPlayer &&
    Application.platform != RuntimePlatform.WindowsEditor)
{
    DebugManager.LogWarning(DebugCategory.Audio,
        "Output device enumeration only supported on Windows platform", null);
    return fallbackDeviceList;
}
```

---

## Device Selection Limitations

```csharp
public static bool SetOutputDevice(string deviceId)
{
    // NOTE: Setting default audio device programmatically requires:
    // 1. IPolicyConfig interface (undocumented Windows API)
    // 2. Or AudioSwitcher library (additional dependencies)
    // 3. Or instruct users to change in Windows Sound settings

    // This implementation logs the selection but cannot change system default
    DebugManager.LogWarning(DebugCategory.Audio,
        "Unity's AudioListener uses the Windows system default device.", null);

    return true;
}
```

**Why Limited**: Windows Core Audio provides device enumeration, but changing the default output device requires undocumented APIs (IPolicyConfig) that Microsoft doesn't officially support.

---

## COM Memory Management

Proper COM object cleanup is critical:

```csharp
try
{
    // Use COM objects
    IMMDevice device;
    collection.Item(i, out device);

    // ... process device ...
}
finally
{
    // Always release COM objects
    Marshal.ReleaseComObject(device);
}

// Release collection and enumerator
Marshal.ReleaseComObject(deviceCollection);
Marshal.ReleaseComObject(enumerator);
```

---

## Usage Example

```csharp
// Get Windows audio devices
var devices = WindowsAudioDeviceManager.GetOutputDevices();

foreach (var device in devices)
{
    Debug.Log($"{device.FriendlyName} {(device.IsDefault ? "(Default)" : "")}");
    Debug.Log($"  ID: {device.Id}");
}
```

---

## Integration Points

### Dependencies
- `System.Runtime.InteropServices` - COM interop
- `ole32.dll` - CoCreateInstance
- `WOS.Debugging.DebugManager` - Logging

### Comparison with FMOD Solution
| Feature | WindowsAudioDeviceManager | FMODAudioDeviceManager |
|---------|---------------------------|------------------------|
| Platform | Windows only | Cross-platform |
| Device Switching | Cannot change default | Runtime switching |
| Dependencies | Native COM | FMOD plugin |
| Recommended | Reference only | **Use this** |

---

## Design Notes

### WASAPI vs FMOD
- WASAPI is Windows-specific Core Audio API
- FMOD provides cross-platform abstraction
- FMOD allows runtime device switching
- This class primarily for reference/fallback

### COM Interop
- Uses [ComImport] interfaces
- Requires proper object lifetime management
- Marshal.ReleaseComObject() essential

### Device States
- Only enumerates DEVICE_STATE_ACTIVE devices
- Disconnected/disabled devices not listed
- Default device identified via separate query
