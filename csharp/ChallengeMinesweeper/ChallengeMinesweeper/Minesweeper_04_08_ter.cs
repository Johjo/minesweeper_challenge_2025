namespace ChallengeMinesweeper;
/* Erreur :
     Expected string length 0 but was 9. Strings differ at index 0.
  Expected: <string.Empty>
  But was:  "fdsfdsfds"
 */

// Action : Je dois renvoyer une chaîne vide


public class TestMineSweeper0408Ter
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("", "")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(Minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string Minesweeper(string unsolvedField)
    {
        return "";
    }
}