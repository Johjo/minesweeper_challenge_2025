namespace ChallengeMinesweeper;
/* Erreur :
     String lengths are both 1. Strings differ at index 0.
  Expected: "*"
  But was:  "0"

 */

/*
 Action : Je découvre que je peux avoir une mine dans une case.
 Je vais gérer cette mine
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

        return "*";
    }
}