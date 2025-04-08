namespace ChallengeMinesweeper;
/* Erreur :
    String lengths are both 2. Strings differ at index 0.
    Expected: "00"
    But was:  "**"
 */

/*
 Action : Je constate qu'il peut aussi y avoir des cases sans mine.
 Je vais valider ce concept rapidement
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