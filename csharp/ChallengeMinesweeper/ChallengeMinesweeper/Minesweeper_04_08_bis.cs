namespace ChallengeMinesweeper;

// Transformation : (nil->constant)  

public class TestMineSweeper0408Bis
{
    [SetUp]
    public void Setup()
    {
    }
    
    [TestCase("" ,"")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string minesweeper(string unsolvedField)
    {
        return "";
    }
}