import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class Day_03 {

  char findMinOrMaxBit(int position, String[] data, Boolean getMax) {
    long numOfZero = Arrays.stream(data).filter(c -> c.charAt(position) == '0').toList().size();
    long numOfOne = Arrays.stream(data).filter(c -> c.charAt(position) == '1').toList().size();

    if (getMax) {
      return numOfZero > numOfOne ? '0' : '1';
    } else {
      return numOfZero < numOfOne ? '0' : '1';
    }

  }

  char findMinOrMaxBit_2(int position, String[] data, Boolean getMax) {
    long numOfZero = Arrays.stream(data).filter(c -> c.charAt(position) == '0').toList().size();
    long numOfOne = Arrays.stream(data).filter(c -> c.charAt(position) == '1').toList().size();

    if (getMax) {
      return numOfZero <= numOfOne ? '1' : '0';
    } else {
      return numOfZero <= numOfOne ? '0' : '1';
    }

  }

  List<String> filterData(Integer position, Character num, String[] data){
    return Arrays.stream(data).filter(c -> c.charAt(position) == num).toList();
  }

  Integer calculateSecondProblem(String[] data){

    String[] oxygenData = data;
    int idx = 0;

    while(oxygenData.length != 1){
      Character bitToFilter = findMinOrMaxBit_2(idx, oxygenData, Boolean.TRUE);
      oxygenData = filterData(idx, bitToFilter, oxygenData).toArray(new String[0]);

      idx += 1;
    }
    String oxygenRating = oxygenData[0];


    String[] co2Data = data;
    idx = 0;
    while(co2Data.length != 1){
      Character bitToFilter = findMinOrMaxBit_2(idx, co2Data, Boolean.FALSE);
      co2Data = filterData(idx, bitToFilter, co2Data).toArray(new String[0]);
      idx += 1;
    }
    String co2Rating = co2Data[0];

    return Integer.parseInt(String.valueOf(oxygenRating), 2) * Integer.parseInt(String.valueOf(co2Rating), 2);
  }

  Integer calculateFirstProblem(String[] data) {
    StringBuilder maxBit = new StringBuilder();
    StringBuilder minBit = new StringBuilder();

    for (int i = 0; i < data[0].length(); i++) {
      maxBit.append(findMinOrMaxBit(i, data, Boolean.TRUE));
      minBit.append(findMinOrMaxBit(i, data, Boolean.FALSE));
    }

    return Integer.parseInt(String.valueOf(maxBit), 2) * Integer.parseInt(String.valueOf(minBit), 2);
  }

  public static void main(String[] args) throws IOException {
    String file = Files.readString(Paths.get("src/main/resources/input.txt"));
    String[] split_string = file.split("\n");

    Day_03 day03 = new Day_03();
    System.out.println(day03.calculateFirstProblem(split_string));
    System.out.println(day03.calculateSecondProblem(split_string));
  }
}
