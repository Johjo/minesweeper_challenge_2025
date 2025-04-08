namespace ChallengeMinesweeper;
/* Observation :
Avant cela, je constate que j'ai 2 fois le solve cell
 */

/* Action
Cela se produit quand mon champ de mine contient une ligne de 2 cellules.
Je vais mettre cela en évidence
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

        if (unsolvedField.Length == 2)
            return SolveCell(unsolvedField) + SolveCell(unsolvedField);
        
        return SolveCell(unsolvedField);
    }

    private static string SolveCell(string unsolvedField)
    {
        if (unsolvedField[0] == '.')
            return "0";
        return "*";
    }
}