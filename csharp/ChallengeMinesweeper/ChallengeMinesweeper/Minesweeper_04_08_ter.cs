namespace ChallengeMinesweeper;
/* Erreur :
     Expected string length 2 but was 1. Strings differ at index 1.
  Expected: "**"
  But was:  "*"
 */

/*
 Action : Je découvre que je peux avoir plusieurs cases dans une ligne.
 je vais gérer cette ligne
*/


public class TestMineSweeper0408Ter
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("", "")]
    [TestCase(".", "0")]
    [TestCase("*", "*")]
    [TestCase("**", "**")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(Minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string Minesweeper(string unsolvedField)
    {
        if (unsolvedField == "") 
            return "";

        if (unsolvedField == ".")
            return "0";
        if (unsolvedField == "*")
            return "*";

        return "**";
    }
}