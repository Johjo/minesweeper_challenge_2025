namespace ChallengeMinesweeper;
/* Observation :
je vois à nouveau la possibilité de traiter une seule mine.

 */

/* Action
 je vais extraire une méthode pour traiter une seule cellule
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

        if (unsolvedField == "**")
            return "**";

        if (unsolvedField == "..")
            return "00";
        
        if (unsolvedField == ".")
            return "0";
        return "*";
    }
}