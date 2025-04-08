namespace ChallengeMinesweeper;
/* Observation :
Erreur
      Expected string length 2 but was 1. Strings differ at index 1.
  Expected: "00"
  But was:  "0"

 */

/* Action
 Je ne peux pas faire cette transformation car la double ligne passe ici.
 Hypothèse : Je vais inverser le code
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
    [TestCase("..", "00")]
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

        if (unsolvedField == "**")
            return "**";

        return "00";
    }
}