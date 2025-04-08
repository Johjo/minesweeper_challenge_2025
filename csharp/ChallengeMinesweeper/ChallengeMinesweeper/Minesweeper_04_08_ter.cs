namespace ChallengeMinesweeper;
/* Erreur :
     Expected string length 1 but was 0. Strings differ at index 0.
  Expected: "0"
  But was:  <string.Empty>
 */

/*
 Action : Je renvoyais un champ de mine vide.
 Maintenant, il doit contenir une case vide
*/


public class TestMineSweeper0408Ter
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("", "")]
    [TestCase(".", "0")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(Minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string Minesweeper(string unsolvedField)
    {
        if (unsolvedField == "") 
            return "";

        return "0";
    }
}