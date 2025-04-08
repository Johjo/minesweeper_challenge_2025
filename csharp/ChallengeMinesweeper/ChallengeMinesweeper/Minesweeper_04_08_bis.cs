namespace ChallengeMinesweeper;

// Je n'ai pas trouvé de transformation prioritaire, j'aborde en fait un nouveau concept
// Transformation : (unconditional->if) splitting the execution path  

public class TestMineSweeper0408Bis
{
    [SetUp]
    public void Setup()
    {
    }
    
    [TestCase("" ,"")]
    [TestCase("*" ,"*")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string minesweeper(string unsolvedField)
    {
        if (unsolvedField == "")
            return "";
        return "*";
    }
}