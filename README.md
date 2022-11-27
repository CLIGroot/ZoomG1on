<h1>Being developed in linux environment!</h1>

<p><code>device = os.open("/dev/midi2", os.O_RDWR)</code><br>"/dev/midi2" is the path to your device,probably will be in the same path.</p>

<div>
  <h3> TUNER </h3>
  Turn tuner on : <code>python3 main.py tuner on</code>
  <br>
  Turn tuner off: <code>python3 main.py tuner off</code>

  <h3> PATCHES </h3>
  <p>If you need to know patches name <code>python3 main.py patch list</code><br>
  will return something like this.<br>

  A0<br>
  A1<br>
  A2<br>
  A3<br>
  A4<br>
  A5<br>
  A6<br>
  A7<br>
  A8<br>
  A9<br>
  ...
  </p>

  Change patches for A0: <code>python3 main.py patch A0</code>
  <br>
  Change patches for B0: <code>python3 main.py patch B0</code>
</div>
<br><br>
<div>
    <p>
    <img src=https://img.shields.io/badge/Version-2022.2.7-blue></img>
    <img src=https://img.shields.io/badge/Plataform-Linux_x86__64-blue></img>
    <br><br>
    <a href="https://github.com/Groot-cmd">
      <img src=https://img.shields.io/github/followers/CLIGroot?style=social></img>
    </a>
  </p>
</div>
