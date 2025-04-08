namespace ChallengeMinesweeper;
/* Observation :
 Je cosntate que j'ai les concepts de résoudre une cellule et que j'en ai besoin lorsque je travaille sur une ligne
 */

/* Action
 Je vais extraire ce concept
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

        if (unsolvedField[0] == '.')
            return "0";
        if (unsolvedField == "*")
            return "*";

        if (unsolvedField == "**")
            return "**";

        return "00";
    }
}