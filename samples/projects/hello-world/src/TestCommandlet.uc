class TestCommandlet extends Commandlet;

event int main(string parameters) {
  // UT3 compile will have an error on log - it uses `log instead.
//  log("Hello, worlds!");
  
  return 0;
}

defaultproperties
{
}