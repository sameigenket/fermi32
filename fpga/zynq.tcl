# Setup Project and add files
set project_name = "fermi_32"
set part "XC7Z020-1CLG400C"

add_files [glob ./src/*.sv]

add_files -fileset constrs_1 [glob ./consrt/*.xdc]

puts "Finished Build Script"
