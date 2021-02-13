package anue.web.model;

import java.util.Objects;
import anue.web.model.ContactDto;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * Zeigt alle Basisinformationen zu einem Studenten 
 */
@ApiModel(description = "Zeigt alle Basisinformationen zu einem Studenten ")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-02-13T14:21:22.739836+01:00[Europe/Berlin]")

public class StudentDto   {
  @JsonProperty("studentId")
  private String studentId;

  @JsonProperty("adresse")
  private ContactDto adresse;

  public StudentDto studentId(String studentId) {
    this.studentId = studentId;
    return this;
  }

  /**
   * Get studentId
   * @return studentId
  */
  @ApiModelProperty(required = true, value = "")
  @NotNull


  public String getStudentId() {
    return studentId;
  }

  public void setStudentId(String studentId) {
    this.studentId = studentId;
  }

  public StudentDto adresse(ContactDto adresse) {
    this.adresse = adresse;
    return this;
  }

  /**
   * Get adresse
   * @return adresse
  */
  @ApiModelProperty(value = "")

  @Valid

  public ContactDto getAdresse() {
    return adresse;
  }

  public void setAdresse(ContactDto adresse) {
    this.adresse = adresse;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StudentDto student = (StudentDto) o;
    return Objects.equals(this.studentId, student.studentId) &&
        Objects.equals(this.adresse, student.adresse);
  }

  @Override
  public int hashCode() {
    return Objects.hash(studentId, adresse);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StudentDto {\n");
    
    sb.append("    studentId: ").append(toIndentedString(studentId)).append("\n");
    sb.append("    adresse: ").append(toIndentedString(adresse)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

