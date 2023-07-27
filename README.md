<h1 align="left">FED : File Encryption Decryption [v2.0]</h1>

<p align="left">
  <img alt="Python Version" src="https://img.shields.io/badge/Python-3.x-blue.svg">
</p>

<h2>Description</h2>
<p>This Python script is a simple command-line tool that allows you to encrypt and decrypt files using the AES encryption algorithm with Cipher Block Chaining (CBC) mode. The tool uses the <code>tkinter</code> library for file selection dialogs and the <code>Crypto.Cipher</code> module from the <code>pycryptodome</code> package for encryption and decryption operations.</p>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>pycryptodome (<code>pip install pycryptodome</code>)</li>
</ul>

<h2>Usage</h2>
<p>
  <ol>
    <li>Run the script, and it will display a pre-load screen with an ASCII art banner.</li>
    <li>The script will present you with a menu to choose the desired operation:</li>
    <ul>
      <li>Encrypt a file of a specific category (Photo, Music, Video, or PDF).</li>
      <li>Decrypt a previously encrypted file.</li>
      <li>Exit the script.</li>
    </ul>
    <li>If you choose to encrypt a file, the script will prompt you to select the file you want to encrypt. After selecting the file, it will then ask you to choose a location to save the encrypted file. You will also need to provide a 16-digit encryption key for the AES algorithm.</li>
    <li>If you choose to decrypt a file, the script will prompt you to select the encrypted file you want to decrypt. After selecting the file, it will then ask you to choose a location to save the decrypted file. You will also need to provide the 16-digit decryption key used during encryption.</li>
    <li>The script will log the encryption details, including the original file name, encrypted file name, encrypted file path, encryption key, and timestamp, in a file called <code>logs.txt</code> within the script's directory.</li>
  </ol>
</p>

<h2>Supported File Types</h2>
<p>
  <ul>
    <li><strong>Photo:</strong> .jpg, .png</li>
    <li><strong>Music:</strong> .mp3</li>
    <li><strong>Video:</strong> .mp4, .mkv</li>
    <li><strong>PDF:</strong> .pdf</li>
  </ul>
  <em>Note: You can extend the list of supported file types by adding more categories and their associated extensions in the script.</em>
</p>

<h2>Disclaimer</h2>
<p>
  <ul>
    <li>This script is provided as-is and without warranty. Use it at your own risk.</li>
    <li>Ensure that you keep the encryption keys safe and secure. Losing the keys will result in permanent data loss.</li>
  </ul>
</p>

<h2>Author</h2>
<p>
  <ul>
    <li>Name: Rajput Shubhraj Singh</li>
    <li>GitHub: <a href="https://github.com/shuuubhraj">https://github.com/shuuubhraj</a></li>
  </ul>
</p>

<h2>Acknowledgments</h2>
<p>Special thanks to the developers of <code>tkinter</code> and <code>pycryptodome</code> for their excellent libraries.</p>

<hr>


