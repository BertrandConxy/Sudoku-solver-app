import { PythonShell } from "python-shell";

PythonShell.run('app.py', null).then(result=>{
    console.log(result)
  });

