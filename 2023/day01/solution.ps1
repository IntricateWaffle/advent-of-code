# $puzzleinput = Get-Content $PSScriptRoot\input.txt
# $puzzleinput = Get-Content $PSScriptRoot\example-input.txt
$puzzleinput = Get-Content $PSScriptRoot\example-input-2.txt

function Part1 {
    $calibration_values = [System.Collections.Generic.List[Int32]]::new()
    foreach ($line in $puzzleinput){
        $line
        $line_values = [System.Collections.Generic.List[Int32]]::new()
        foreach ($i in $line.GetEnumerator()){
            try {
                $line_values.Add($i.ToString())
            }
            catch { 
            }    
        }
        $line_calibration_value = [string]$line_values[0] + [string]$line_values[-1]
        $calibration_values.Add($line_calibration_value)
    }
    
    $calibration_values | Measure-Object -AllStats 
    
    
}


function Solve {
    Part1
    
}

Solve