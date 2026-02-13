public double? ReadPressure(string sensorId) 
{
    // 1. Validation: Following the "Sanitize Inputs" rule
    if (string.IsNullOrWhiteSpace(sensorId)) 
    {
        Logger.LogWarning("Invalid Sensor ID provided.");
        return null; 
    }

    try 
    {
        // 2. Logic: Simulated hardware interaction
        double pressure = HardwareInterface.GetReading(sensorId);
        
        // 3. Boundary Check: Ensuring safety thresholds
        if (pressure < 0 || pressure > 5000) 
        {
            Logger.LogCritical($"Out-of-range pressure detected: {pressure} PSI");
            return null;
        }

        return pressure;
    }
    catch (TimeoutException tex) 
    {
        // 4. Specific Exception Handling: No "bare" catches
        Logger.LogError($"Hardware timeout for sensor {sensorId}: {tex.Message}");
        return null;
    }
    catch (Exception ex) 
    {
        // Fail-safe: Always log before returning null
        Logger.LogCritical($"Unexpected system failure: {ex.Message}");
        return null;
    }
}

private void LogToIndustrialMonitor(string message, string level)
{
    // This private method ensures all logs follow the company's audit format
    Console.WriteLine($"[{DateTime.Now}] [{level}] {message}");
}